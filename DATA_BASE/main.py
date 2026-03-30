from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Category, Goal, Task, ProgressLog

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. КОНТРОЛЕР для створення користувача (POST запит)
@app.post("/users/")
def create_user(username: str, xp: int = 0, db: Session = Depends(get_db)):
    new_user = User(username=username, total_xp=xp)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "success", "user": new_user}

# 2. КОНТРОЛЕР для створення категорії
@app.post("/categories/")
def create_category(name: str, color: str, db: Session = Depends(get_db)):
    new_cat = Category(name=name, color_hex=color)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return {"status": "category created", "id": new_cat.category_id}

# 3. КОНТРОЛЕР для отримання даних (GET запит)
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# 4. КОНТРОЛЕР для створення Цілі (Goal)
@app.post("/goals/")
def create_goal(title: str, user_id: int, category_id: int, db: Session = Depends(get_db)):
    new_goal = Goal(title=title, user_id=user_id, category_id=category_id, status="In Progress")
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return {"status": "goal created", "goal": new_goal}

# 5. КОНТРОЛЕР для створення Завдання (Task)
@app.post("/tasks/")
def create_task(task_name: str, xp_reward: int, goal_id: int, priority: int = 1, db: Session = Depends(get_db)):
    if xp_reward <= 0:
        raise HTTPException(status_code=400, detail="XP має бути більше 0")
    if priority < 1 or priority > 5:
        raise HTTPException(status_code=400, detail="Пріоритет має бути від 1 до 5")

    new_task = Task(task_name=task_name, xp_reward=xp_reward, goal_id=goal_id, priority=priority)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status": "task created", "task": new_task}

# 6. КОНТРОЛЕР для отримання всіх завдань конкретної цілі
@app.get("/goals/{goal_id}/tasks/")
def get_tasks_for_goal(goal_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.goal_id == goal_id).all()
    
    if not tasks:
        raise HTTPException(status_code=404, detail="Завдань для цієї цілі не знайдено")
    return tasks

# 7. КОНТРОЛЕР для видалення користувача (DELETE запит)
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user_to_delete = db.query(User).filter(User.user_id == user_id).first()
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="Юзера з таким ID не знайдено")
    
    db.delete(user_to_delete)
    db.commit()
    
    return {"status": "success", "message": f"Юзера {user_to_delete.username} успішно видалено"}