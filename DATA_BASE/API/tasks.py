from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create_task(task_name: str, xp_reward: int, goal_id: int, priority: int = 1, db: Session = Depends(get_db)):
    if xp_reward <= 0:
        raise HTTPException(status_code=400, detail="XP має бути більше 0")
    if priority < 1 or priority > 5:
        raise HTTPException(status_code=400, detail="Пріоритет: 1-5")
    
    new_task = Task(task_name=task_name, xp_reward=xp_reward, goal_id=goal_id, priority=priority)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"task": new_task}