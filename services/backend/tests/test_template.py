import random
import sys


def get_sample_data():
    name = "Sample" + str(random.randint(0,sys.maxsize))
    content = "SampleContent" + str(random.randint(0,sys.maxsize))
    premium = random.choice([True, False])
    return {"name": name, "content": content, "premium": premium}


def test_create_template(test_app, auth_headers):
    data = get_sample_data()
    response = test_app.post("/template", headers=auth_headers, json=data)
    
    assert response.status_code == 201
    assert response.json()["name"] == data["name"]
    assert response.json()["content"] == data["content"]
    assert response.json()["premium"] == data["premium"]


def test_get_all_templates(test_app, auth_headers):
    data = get_sample_data()
    response = test_app.post("/template", headers=auth_headers, json=data)

    assert response.status_code == 201
    template_id = response.json()["id"]
    
    response = test_app.get("/template", headers=auth_headers)
    
    assert response.status_code == 200
    response_list = response.json()
    mapped = map(lambda x: x["id"], response_list)
    assert template_id in mapped



def test_get_template_by_id(test_app, auth_headers):
    data = get_sample_data()
    response = test_app.post("/template", headers=auth_headers, json=data)

    assert response.status_code == 201
    template_id = response.json()['id']

    response = test_app.get(
        f"/template/{template_id}", headers=auth_headers)
    
    assert response.status_code == 200


def test_update_template(test_app, auth_headers):
    data1 = get_sample_data()
    response = test_app.post("/template", headers=auth_headers, json=data1)

    response_obj = response.json()
    data2 = get_sample_data()

    response = test_app.put(
        f"/template?template_id={response_obj['id']}",
        headers=auth_headers, json=data2)
    
    assert response.status_code == 200
    assert response.json()["name"] == data2["name"]
    assert response.json()["content"] == data2["content"]
    assert response.json()["premium"] == data2["premium"]


def test_delete_template(test_app, auth_headers):
    data = get_sample_data()
    response = test_app.post("/template", headers=auth_headers, json=data)

    assert response.status_code == 201
    template_id = response.json()["id"]

    response = test_app.delete(
        f"/template/{template_id}", headers=auth_headers)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Template deleted successfully!"
