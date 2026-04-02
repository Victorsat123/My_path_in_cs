from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import ProgressLog

router = APIRouter(prefix="/progress", tags=["Progress Logs"])

@router.post("/")
def create_progress_log(task_id: int, success_rate: int, notes: str = "", db: Session = Depends(get_db)):
    if success_rate < 0 or success_rate > 100:
        raise HTTPException(status_code=400, detail="Відсоток успіху: 0-100")
        
    new_log = ProgressLog(task_id=task_id, success_rate=success_rate, notes=notes)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return {"log": new_log}