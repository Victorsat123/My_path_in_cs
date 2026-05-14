def test_create_user(client):
    response = client.post("/users/?username=TestUser&xp=10")
    assert response.status_code == 200
    assert response.json()["user"]["username"] == "TestUser"

def test_get_users(client):
    client.post("/users/?username=User1&xp=0")
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_delete_user(client):
    client.post("/users/?username=ToDelete&xp=0")
    response = client.delete("/users/1")
    assert response.status_code == 200