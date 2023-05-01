from fastapi import APIRouter
from fastapi import Depends
from app.schemas import CreateCategories, DeleteCategories, EditCategories, \
    ListCategories
from app.services import create_categories, delete_categories, edit_categories, category_list
from sqlalchemy.orm import Session
from core.config import get_db

categories_app = APIRouter()


@categories_app.post("/create_categories")
async def create_category(data: CreateCategories, db: Session = Depends(get_db)):
    try:
        response = create_categories(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@categories_app.post("/edit_categories")
async def edit_category(data: EditCategories, db: Session = Depends(get_db)):
    try:
        response = edit_categories(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@categories_app.delete("/delete_categories")
async def delete_category(data: DeleteCategories, db: Session = Depends(get_db)):
    try:
        response = delete_categories(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@categories_app.post("/list_categories")
async def list_category(data: ListCategories, db: Session = Depends(get_db)):
    try:
        response = category_list(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}
