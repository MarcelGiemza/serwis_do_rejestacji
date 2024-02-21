from flask import Flask, request, Response
from controller import UserController
from STATUS_CODES import *

user_controller = UserController()
app = Flask(__name__)


@app.get("/")
def ping():
    return {"ping": True}


@app.get("/users/<int:id>")
def get(id):
    user = user_controller.get(id)
    if user.get("status", None):
        return Response(status=NOT_FOUND)


@app.get("/users")
def get_all():
    return user_controller.get_all()


@app.post("/users")
def post():
    return Response(status=user_controller.post(request.get_json()))


@app.patch("/users/<int:id>")
def patch(id):
    return Response(status=user_controller.patch(id, request.get_json()))


@app.delete("/users/<int:id>")
def delete(id):
    return Response(status=user_controller.delete(id))


if __name__ == "__main__":
    app.run("localhost", 8000)
