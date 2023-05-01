import pdb

from fastapi import APIRouter
from fastapi import Depends,UploadFile,Form,File
from typing import List
from app.schemas import CreateProduct, EditProduct, EditImage, GetProduct, ProductList, DeleteProduct
from app.services import create_product,edit_product,delete_product,list_product,get_product
from sqlalchemy.orm import Session
from core.config import engine, SessionLocal, get_db

product_app = APIRouter()


@product_app.post("/create_product")
async def create_level(files: List[UploadFile]=File(...),data: CreateProduct=Depends(), db: Session = Depends(get_db)):
    try:
        response = create_product(db, data,files)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@product_app.post("/edit_product")
async def edit_level(data: EditProduct, db: Session = Depends(get_db)):
    try:
        response = edit_product(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@product_app.post("/get_product")
async def get_level(data: GetProduct, db: Session = Depends(get_db)):
    try:
        pdb.set_trace()
        response = get_product(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@product_app.delete("/delete_product")
async def delete_level(data: DeleteProduct, db: Session = Depends(get_db)):
    try:
        response = delete_product(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@product_app.post("/list_product")
async def list_level(data: ProductList, db: Session = Depends(get_db)):
    try:
        response = list_product(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}
