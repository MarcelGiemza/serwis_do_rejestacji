from main import CREATED, NO_CONTENT, WRONG_REQUEST, OK, NOT_FOUND, app, create_api, User
create_api("user", "users", {
    1: {"firstName": "test", "lastName": "test", "birthYear": 2000, "group": "user"},
    2: {"firstName": "test2", "lastName": "test2", "birthYear": 1500, "group": "premium"}
}, User)


def test_ping():
    client = app.test_client()
    actual = client.get("/")
    assert actual.status_code == OK


def test_post():
    client = app.test_client()
    actual = client.post("/users/",
                         json={"firstName": "test", "lastName": "test", "birthYear": 2000, "group": "user"})
    assert actual.status_code == CREATED


def test_post_wrong():
    client = app.test_client()
    actual = client.post("/users/", json={"name": "test"})
    assert actual.status_code == WRONG_REQUEST


def test_patch_firstName():
    client = app.test_client()
    actual = client.patch("/users/1", json={"firstName": "Marcel"})
    assert actual.status_code == NO_CONTENT


def test_patch_lastName():
    client = app.test_client()
    actual = client.patch("/users/1", json={"lastName": "Marcel"})
    assert actual.status_code == NO_CONTENT


def test_patch_birthYear():
    client = app.test_client()
    actual = client.patch("/users/1", json={"birthYear": 2000})
    assert actual.status_code == NO_CONTENT


def test_patch_birthYear_not_int():
    client = app.test_client()
    actual = client.patch("/users/1", json={"birthYear": "2000"})
    assert actual.status_code == WRONG_REQUEST


def test_patch_group_user():
    client = app.test_client()
    actual = client.patch("/users/2", json={"group": "user"})
    assert actual.status_code == NO_CONTENT


def test_patch_group_premium():
    client = app.test_client()
    actual = client.patch("/users/1", json={"group": "premium"})
    assert actual.status_code == NO_CONTENT


def test_patch_group_admin():
    client = app.test_client()
    actual = client.patch("/users/1", json={"group": "admin"})
    assert actual.status_code == NO_CONTENT


def test_patch_no_user():
    client = app.test_client()
    actual = client.patch("/users/10", json={"firstName": "Marcel"})
    assert actual.status_code == WRONG_REQUEST


def test_patch_no_data():
    client = app.test_client()
    actual = client.patch("/users/1", json={})
    assert actual.status_code == WRONG_REQUEST


def test_delete():
    client = app.test_client()
    actual = client.delete("/users/1")
    assert actual.status_code == NO_CONTENT


def test_delete_no_user():
    client = app.test_client()
    actual = client.delete("/users/10")
    assert actual.status_code == NO_CONTENT
