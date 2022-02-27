
class ProfileUtils:
    @staticmethod
    def create_profile(test_app, auth_headers, profile_data):
        response = test_app.post("/profile", headers=auth_headers, json=profile_data)
        assert response.status_code == 201
        return response

    @staticmethod
    def get_profile_me(test_app, auth_headers):
        response = test_app.get("/profile/me", headers=auth_headers)
        assert response.status_code == 200
        return response

    @staticmethod
    def delete_profile(test_app, auth_headers, profile_id):
        response = test_app.delete(f"profile/{profile_id}", headers=auth_headers)
        assert response.status_code == 200
        assert response.json()["message"] == "Profile deleted successfully"


class TemplateUtils:

    @staticmethod
    def create_template(test_app, auth_headers, template):
        response = test_app.post("/template", headers=auth_headers, json=template)
        assert response.status_code == 201
        return response

