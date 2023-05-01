from fastapi import APIRouter
from fastapi import Depends
from app.schemas import CreateLevel,EditLevel,GetLevel
from app.services import get_levels,edit_levels,create_levels
from sqlalchemy.orm import Session
from core.config import engine, SessionLocal,get_db

level_app = APIRouter()
@level_app.post("/create_level")
async def create_level(data: CreateLevel, db: Session = Depends(get_db)):
    try:
        response = create_levels(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@level_app.post("/edit_level")
async def edit_level(data: EditLevel, db: Session = Depends(get_db)):
    try:
        response = edit_levels(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@level_app.post("/get_level")
async def get_level(data: GetLevel, db: Session = Depends(get_db)):
    try:
        response = get_levels(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}

