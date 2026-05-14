def test_create_progress(client):
    client.post("/users/?username=ProgOwner&xp=0")
    client.post("/categories/?name=ProgCat&color=0000FF")
    client.post("/goals/?title=ProgGoal&user_id=1&category_id=1")
    client.post("/tasks/?task_name=ProgTask&xp_reward=50&goal_id=1&priority=1")
    
    response = client.post("/progress/?task_id=1&success_rate=85&notes=Done")
    assert response.status_code == 200
    assert response.json()["log"]["success_rate"] == 85
    
def test_invalid_progress(client):
    client.post("/users/?username=FailOwner&xp=0")
    client.post("/categories/?name=FailCat&color=0000FF")
    client.post("/goals/?title=FailGoal&user_id=1&category_id=1")
    client.post("/tasks/?task_name=FailTask&xp_reward=50&goal_id=1&priority=1")
    
    # Перевірка на (відсоток більше 100)
    response = client.post("/progress/?task_id=1&success_rate=150")
    assert response.status_code == 400