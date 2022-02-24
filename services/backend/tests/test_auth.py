import random
import sys


def get_random_user():
    username = "SampleUser" + str(random.randint(0, sys.maxsize))
    password = "SamplePassword" + str(random.randint(0, sys.maxsize))
    return {"username": username, "password": password}


def test_register_user(test_app):
    user = get_random_user()
    response = test_app.post("/auth/register", json=user)

    assert response.status_code == 201
    assert response.json()["username"] == user["username"]
