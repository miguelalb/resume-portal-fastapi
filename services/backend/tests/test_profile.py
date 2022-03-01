from .fake_data_generator import get_sample_profile, get_sample_template
from .utils import ProfileUtils, TemplateUtils


def delete_profile_if_exists(test_app, auth_headers):
    response = ProfileUtils.get_profile_me(test_app, auth_headers)
    if "id" in response.json():
        ProfileUtils.delete_profile(test_app, auth_headers, response.json()["id"])


def test_create_profile(test_app, auth_headers):
    delete_profile_if_exists(test_app, auth_headers)
    
    template_data = get_sample_template()
    response = TemplateUtils.create_template(test_app, auth_headers, template_data)
    template_id = response.json()["id"]
    
    profile_data = get_sample_profile()
    profile_data["template_id"] = template_id
    response = ProfileUtils.create_profile(test_app, auth_headers, profile_data)

    assert response.status_code == 201
    assert response.json()["first_name"] == profile_data["first_name"]
    assert response.json()["public_name"] == profile_data["public_name"]
    assert (
        response.json()["educations"][0]["college"] == profile_data["educations"][0]["college"]
    )


def test_update_profile(test_app, auth_headers):
    delete_profile_if_exists(test_app, auth_headers)
    
    template_data = get_sample_template()
    response = TemplateUtils.create_template(test_app, auth_headers, template_data)
    template_id = response.json()["id"]
    
    profile_data = get_sample_profile()
    profile_data["template_id"] = template_id
    response = ProfileUtils.create_profile(test_app, auth_headers, profile_data)
    profile_id = response.json()["id"]

    new_template = get_sample_template()
    response = TemplateUtils.create_template(test_app, auth_headers, new_template)
    new_template_id = response.json()["id"]
    
    new_profile = get_sample_profile()
    new_profile["template_id"] = new_template_id 
    
    response = test_app.put(
        f"/profile/{profile_id}", headers=auth_headers, json=new_profile
    )
    assert response.status_code == 200
    assert response.json()["first_name"] == new_profile["first_name"]
    assert response.json()["public_name"] == new_profile["public_name"]
    assert response.json()["last_name"] == new_profile["last_name"]
    assert response.json()["template"]["id"] == new_template_id


def test_get_profile_by_public_name(test_app, auth_headers):
    pass #TODO
