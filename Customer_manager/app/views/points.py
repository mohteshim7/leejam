import pdb

from fastapi import APIRouter
from fastapi import Depends
from app.schemas import CreatePoint, EditPoint, CancelPoint,ListPoint
from app.services import create_points, cancel_points, edit_points,point_list
from sqlalchemy.orm import Session
from core.config import get_db

point_app = APIRouter()


@point_app.post("/create_point")
async def create_point(data: CreatePoint, db: Session = Depends(get_db)):
    try:
        response = create_points(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@point_app.post("/edit_point")
async def edit_point(data: EditPoint, db: Session = Depends(get_db)):
    try:
        response = edit_points(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@point_app.post("/cancel_point")
async def cancel_point(data: CancelPoint, db: Session = Depends(get_db)):
    try:
        response = cancel_points(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}

@point_app.post("/list_point")
async def list_point(data: ListPoint, db: Session = Depends(get_db)):
    try:
        response = point_list(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}