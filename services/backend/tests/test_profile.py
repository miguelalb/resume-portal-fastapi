from .data_generator import get_sample_profile, get_sample_template


def test_create_profile(test_app, auth_headers):
    template = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=template)
    assert response.status_code == 201

    data = get_sample_profile()
    data["template_id"] = response.json()["id"]
    response = test_app.post("/profile", headers=auth_headers, json=data)

    assert response.status_code == 201
    assert response.json()["first_name"] == data["first_name"]
    assert response.json()["public_name"] == data["public_name"]
    assert (
        response.json()["educations"][0]["college"] == data["educations"][0]["college"]
    )


# def test_get_profile_by_public_name(test_app, auth_headers):
#     template = get_sample_template()
#     response = test_app.post("/template", headers=auth_headers, json=template)
#     assert response.status_code == 201

#     data = get_sample_profile()
#     data["template_id"] = response.json()["id"]
#     response = test_app.post("/profile", headers=auth_headers, json=data)

#     assert response.status_code == 201
#     public_name = response.json()["public_name"]

#     response = test_app.get(f"/profile/{public_name}")
#     assert response.status_code == 200
#     assert response.json()["first_name"] == data["first_name"]
#     assert response.json()["public_name"] == data["public_name"]

#     response = test_app.get("/profile/wrong_profile_public_name")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "User Profile not found."


def test_get_my_profile(test_app, auth_headers):
    template = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=template)
    assert response.status_code == 201

    data = get_sample_profile()
    data["template_id"] = response.json()["id"]
    response = test_app.post("/profile", headers=auth_headers, json=data)
    assert response.status_code == 201

    response = test_app.get("/profile/me", headers=auth_headers)
    assert response.status_code == 200


def test_delete_profile(test_app, auth_headers):
    template = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=template)
    assert response.status_code == 201

    data = get_sample_profile()
    data["template_id"] = response.json()["id"]
    response = test_app.post("/profile", headers=auth_headers, json=data)

    assert response.status_code == 201
    profile_id = response.json()["id"]

    response = test_app.delete(f"profile/{profile_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Profile deleted successfully"


def test_update_profile(test_app, auth_headers):
    template = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=template)
    assert response.status_code == 201
    template_id = response.json()["id"]

    data = get_sample_profile()
    data["template_id"] = template_id
    response = test_app.post("/profile", headers=auth_headers, json=data)

    assert response.status_code == 201
    profile_id = response.json()["id"]

    data_updated = get_sample_profile()
    data_updated["template_id"] = template_id
    response = test_app.put(
        f"/profile/{profile_id}", headers=auth_headers, json=data_updated
    )
    assert response.status_code == 200
    assert response.json()["first_name"] == data_updated["first_name"]
    assert response.json()["public_name"] == data_updated["public_name"]
    assert response.json()["last_name"] == data_updated["last_name"]
