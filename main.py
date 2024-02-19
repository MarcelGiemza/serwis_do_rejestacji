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
        return {"error": None, "data": list(map(lambda user: merge_dicts({"id": user[0]}, user[1]), list(users.items())))}


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
            "birthYear": {"type": "intiger"},
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


user_item_api = ItemAPI.as_view("user-item", users, User, "user")
user_group_api = GroupAPI.as_view("user-group", users, User, "users")
app.add_url_rule(f"/users/<int:id>", view_func=user_item_api)
app.add_url_rule(f"/users/", view_func=user_group_api)
app.add_url_rule(f"/", view_func=Ping.as_view("ping"))

if __name__ == "__main__":
    app.run("localhost", 8000)
