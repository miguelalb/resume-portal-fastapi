def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
