from .data_generator import get_sample_template


def test_create_template(test_app, auth_headers):
    data = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=data)

    assert response.status_code == 201
    assert response.json()["name"] == data["name"]
    assert response.json()["content"] == data["content"]
    assert response.json()["premium"] == data["premium"]


def test_get_all_templates(test_app, auth_headers):
    data = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=data)

    assert response.status_code == 201
    template_id = response.json()["id"]

    response = test_app.get("/template", headers=auth_headers)

    assert response.status_code == 200
    response_list = response.json()
    mapped = map(lambda x: x["id"], response_list)
    assert template_id in mapped


def test_get_template_by_id(test_app, auth_headers):
    data = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=data)

    assert response.status_code == 201
    template_id = response.json()["id"]

    response = test_app.get(f"/template/{template_id}", headers=auth_headers)

    assert response.status_code == 200


def test_update_template(test_app, auth_headers):
    data1 = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=data1)

    response_obj = response.json()
    data_updated = get_sample_template()

    response = test_app.put(
        f"/template?template_id={response_obj['id']}",
        headers=auth_headers,
        json=data_updated,
    )

    assert response.status_code == 200
    assert response.json()["name"] == data_updated["name"]
    assert response.json()["content"] == data_updated["content"]
    assert response.json()["premium"] == data_updated["premium"]


def test_delete_template(test_app, auth_headers):
    data = get_sample_template()
    response = test_app.post("/template", headers=auth_headers, json=data)

    assert response.status_code == 201
    template_id = response.json()["id"]

    response = test_app.delete(f"/template/{template_id}", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["message"] == "Template deleted successfully!"
