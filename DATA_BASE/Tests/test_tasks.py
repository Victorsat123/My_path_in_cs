def test_create_task(client):
    client.post("/users/?username=TaskOwner&xp=0")
    client.post("/categories/?name=Study&color=0000FF")
    client.post("/goals/?title=Master DB&user_id=1&category_id=1")
    
    response = client.post("/tasks/?task_name=Write Tests&xp_reward=50&goal_id=1&priority=1")
    assert response.status_code == 200
    assert response.json()["task"]["task_name"] == "Write Tests"
    
def test_task_invalid_xp(client):
    client.post("/users/?username=TaskOwner2&xp=0")
    client.post("/categories/?name=Study2&color=0000FF")
    client.post("/goals/?title=Master DB2&user_id=1&category_id=1")
    
    # Перевірка на (мінусовий досвід)
    response = client.post("/tasks/?task_name=Bad Task&xp_reward=-10&goal_id=1&priority=1")
    assert response.status_code == 400