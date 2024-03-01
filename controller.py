from STATUS_CODES import *


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merges two dicts toghether"""
    return {**dict1, **dict2}


class UserController:
    def __init__(self, db):
        self.db = db

    def get(self, id):
        user = self.db.get(id)
        if not user:
            return {"status": NOT_FOUND}
        return {"user": user}

    def patch(self, id, data):
        user = self.db.get(id)
        if user:
            user.update(data)
            status = self.db.update_user(id, user)
            return status
        return WRONG_REQUEST

    def delete(self, id):
        self.db.delete(id)
        return NO_CONTENT

    def get_all(self):
        return {"users": list(map(lambda user: merge_dicts({"id": user[0]}, user[1]), list(self.db.database.items())))}


    def post(self, data):
        return self.db.add_user(data)
