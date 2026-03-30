from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Category, Goal, Task, ProgressLog

app = FastAPI()

