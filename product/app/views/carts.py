from fastapi import APIRouter
from fastapi import Depends
from app.schemas import CreateCart, DeleteCart, EditCart, \
    ListCart
from app.services import add_cart, delete_cart, edit_cart, cart_list
from sqlalchemy.orm import Session
from core.config import get_db

cart_app = APIRouter()


@cart_app.post("/add_cart")
async def add_carts(data: CreateCart, db: Session = Depends(get_db)):
    try:
        response = add_cart(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@cart_app.post("/edit_cart")
async def edit_carts(data: EditCart, db: Session = Depends(get_db)):
    try:
        response = edit_cart(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@cart_app.delete("/delete_cart")
async def delete_carts(data: DeleteCart, db: Session = Depends(get_db)):
    try:
        response = delete_cart(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}


@cart_app.post("/list_cart")
async def list_carts(data: ListCart, db: Session = Depends(get_db)):
    try:
        response = cart_list(db, data)
        return {"status": True, "result": response}
    except Exception as e:
        print(f"exceptions are {e}")
        return {"status": False, "result": "something went wrong"}
