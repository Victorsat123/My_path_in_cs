from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(username: str, xp: int = 0, db: Session = Depends(get_db)):
    new_user = User(username=username, total_xp=xp)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "success", "user": new_user}

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_to_delete = db.query(User).filter(User.user_id == user_id).first()
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")
    db.delete(user_to_delete)
    db.commit()
    return {"status": "success"}