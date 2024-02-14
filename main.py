from flask.views import MethodView
from flask import Flask, request
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from database import users
from enum import Enum

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merges two dicts toghether"""
    return {**dict1, **dict2}

app = Flask(__name__)


class ItemAPI(MethodView):
    def __init__(self, db, model):
        self.db = db
        self.model = model

    def _get(self, id):
        user = users.get(id, None)
        if not user:
            return {"error": "id error", "data": None}
        user.update({"id": id})
        return {"error": None, "data": user}

    def get(self, id):
        return self._get(id)

    def patch(self, id):

        user = self._get(id)


class GroupAPI(MethodView):
    def __init__(self, db, model):
        self.db = db
        self.model = model

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
            "birthYear": {"type": "intiger"},
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


user_item_api = ItemAPI.as_view("user-item", users, User)
user_group_api = GroupAPI.as_view("user-group", users, User)
app.add_url_rule(f"/users/<int:id>", view_func=user_item_api)
app.add_url_rule(f"/users/", view_func=user_group_api)

if __name__ == "__main__":
    app.run("localhost", 8000)
