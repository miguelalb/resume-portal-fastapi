from .data_generator import get_sample_profile


def test_create_profile(test_app, auth_headers):
    data = get_sample_profile()
    response = test_app.post("/profile", headers=auth_headers, json=data)

    assert response.status_code == 201
    assert response.json()["first_name"] == data["first_name"]
    assert response.json()["public_name"] == data["public_name"]
    assert response.json()["educations"][0]["college"] == data["educations"][0]["college"]
