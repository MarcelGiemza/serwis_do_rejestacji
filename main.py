from flask.views import MethodView
from flask import Flask, request, Response
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from database import users


OK = 200
CREATED = 201
NO_CONTENT = 204
WRONG_REQUEST = 400
NOT_FOUND = 404


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merges two dicts toghether"""
    return {**dict1, **dict2}


app = Flask(__name__)


class ItemAPI(MethodView):
    def __init__(self, db, model, name):
        self.db = db
        self.model = model
        self.name = name

    def _get(self, id):
        item = self.db.get(id, None)
        if not item:
            return {"error": "id error", "data": None}
        item.update({"id": id})
        return {"error": None, "data": item}

    def get(self, id):
        item = self._get(id)
        if item["error"]:
            return Response(status=NOT_FOUND)
        return {self.name: item["data"]}

    def patch(self, id):
        item = self._get(id)
        data = request.get_json()
        if not item["error"] and self.model.validate_patch(data):
            item["data"].update(data)
            self.db.update({id: item["data"]})
            return Response(status=NO_CONTENT)
        return Response(status=WRONG_REQUEST)

    def delete(self, id):
        self.db.pop(id)
        return Response(status=NO_CONTENT)


class GroupAPI(MethodView):
    def __init__(self, db, model, name):
        self.db = db
        self.model = model
        self.name = name

    def get(self):
        return {"data": list(map(lambda user: merge_dicts({"id": user[0]}, user[1]), list(users.items())))}
    
    def _find_lowest_unused_id(self):
        keys = list(self.db.keys())
        for i in range(1, max(keys)+2):
            if keys.count(i) == 0:
                return i

    def post(self):
        data = request.get_json()
        if self.model.validate_post(data):
            id = self._find_lowest_unused_id()
            self.db.update({id: data})
            return Response(status=CREATED)
        return Response(status=WRONG_REQUEST)


class _User:
    def __init__(self):
        pass

    schema_patch = {
        "type": "object",
        "properties": {
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "birthYear": {"type": "number"},
            "group": {"enum": ["user", "premium", "admin"]},
        },
        "minProperties": 1,
        "additionalProperties": False
    }
    schema_post = {
        "type": "object",
        "properties": {
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "birthYear": {"type": "number"},
            "group": {"enum": ["user", "premium", "admin"]},
        },
        "required": ["firstName", "lastName", "birthYear", "group"],
        "additionalProperties": False
    }

    def validate_patch(self, data: dict) -> bool:
        try:
            validate(instance=data, schema=self.schema_patch)
            return True
        except ValidationError as e:
            return False

    def validate_post(self, data: dict) -> bool:
        try:
            validate(instance=data, schema=self.schema_post)
            return True
        except ValidationError as e:
            return False


User = _User()


class Ping(MethodView):
    def get(self):
        return {"ping": True}

def create_api(name, name_plural, db, model):
    item_api = ItemAPI.as_view(f"{name}-item", db, model, name)
    group_api = GroupAPI.as_view(f"{name}-group", db, model, name_plural)
    app.add_url_rule(f"/{name_plural}/<int:id>", view_func=item_api)
    app.add_url_rule(f"/{name_plural}/", view_func=group_api)

app.add_url_rule(f"/", view_func=Ping.as_view("ping"))

if __name__ == "__main__":
    create_api("user", "users", users, User)
    app.run("localhost", 8000)
