def test_create_category(client):
    response = client.post("/categories/?name=Work&color=FF0000")
    assert response.status_code == 200
    assert response.json()["status"] == "category created"