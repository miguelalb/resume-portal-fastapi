
def test_get_user_me(test_app, auth_headers):
    response = test_app.get("/users/me", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["username"] == "admin"


def test_update_user_me(test_app, auth_headers):
    admin_user = {"username": "admin", "password": "admin"}
    response = test_app.put("/users", headers=auth_headers, json=admin_user)

    assert response.status_code == 200
    assert response.json()["username"] == admin_user["username"]
    
