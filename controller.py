from STATUS_CODES import *
from database import User, users


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merges two dicts toghether"""
    return {**dict1, **dict2}


class UserController:
    def __init__(self):
        self.db = users
        self.model = User

    def _get(self, id):
        user = self.db.get(id, None)
        if not user:
            return {"error": "id error", "data": None}
        user.update({"id": id})
        return {"error": None, "data": user}

    def get(self, id):
        user = self._get(id)
        if user["error"]:
            return {"status": NOT_FOUND}
        return {"user": user["data"]}

    def patch(self, id, data):
        user = self._get(id)
        if not user["error"] and self.model.validate_patch(data):
            user["data"].update(data)
            self.db.update({id: user["data"]})
            return NO_CONTENT
        return WRONG_REQUEST

    def delete(self, id):
        try:
            self.db.pop(id)
        except KeyError:
            pass
        return NO_CONTENT

    def get_all(self):
        return {"users": list(map(lambda user: merge_dicts({"id": user[0]}, user[1]), list(self.db.items())))}

    def _find_lowest_unused_id(self):
        keys = list(self.db.keys())
        for i in range(1, max(keys)+2):
            if keys.count(i) == 0:
                return i

    def post(self, data):
        if self.model.validate_post(data):
            id = self._find_lowest_unused_id()
            self.db.update({id: data})
            return CREATED
        return WRONG_REQUEST
