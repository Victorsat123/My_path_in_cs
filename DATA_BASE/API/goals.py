from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Goal, Task

router = APIRouter(prefix="/goals", tags=["Goals"])

@router.post("/")
def create_goal(title: str, user_id: int, category_id: int, db: Session = Depends(get_db)):
    new_goal = Goal(title=title, user_id=user_id, category_id=category_id, status="In Progress")
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return {"status": "goal created", "goal": new_goal}

@router.get("/{goal_id}/tasks/")
def get_tasks_for_goal(goal_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.goal_id == goal_id).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="Завдань немає")
    return tasks