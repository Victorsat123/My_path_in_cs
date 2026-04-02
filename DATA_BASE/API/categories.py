from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Category

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/")
def create_category(name: str, color: str, db: Session = Depends(get_db)):
    new_cat = Category(name=name, color_hex=color)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return {"status": "category created", "id": new_cat.category_id}