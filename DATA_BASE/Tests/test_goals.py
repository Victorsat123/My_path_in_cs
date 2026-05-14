def test_create_goal(client):
    client.post("/users/?username=GoalOwner&xp=0")
    client.post("/categories/?name=Life&color=00FF00")
    
    response = client.post("/goals/?title=Learn Pytest&user_id=1&category_id=1")
    assert response.status_code == 200
    assert response.json()["goal"]["title"] == "Learn Pytest"

def test_get_tasks_for_goal(client):
    client.post("/users/?username=TaskOwner&xp=0")
    client.post("/categories/?name=Study&color=0000FF")
    client.post("/goals/?title=Master DB&user_id=1&category_id=1")
    client.post("/tasks/?task_name=Read Docs&xp_reward=10&goal_id=1")
    
    response = client.get("/goals/1/tasks/")
    assert response.status_code == 200
    assert len(response.json()) == 1