import pdb
import uuid
from sqlalchemy import exc
from app.schemas.carts import CartDB, CreateCart, DeleteCart, EditCart, \
    ListCart
from sqlalchemy.orm import Session


def new_cart_id(db):
    while True:
        id = str(uuid.uuid4())
        data = db.query(CartDB).filter(CartDB.id == id).first()
        if not data:
            return id


def add_cart(db: Session, cart: CreateCart):
    try:
        pdb.set_trace()
        id = new_cart_id(db)
        pc = CartDB(
            id=id,
            user_id=cart.user_id,
            product_id=cart.product_id,
            quantity=cart.quantity,
        )
        db.add(pc)
        db.commit()
        db.refresh(pc)
        return pc.to_dict()
    except exc.IntegrityError as e:
        print(e)
        return "User Exist"
    except Exception as e:
        print(e)
        return "something went wrong"


def edit_cart(db: Session, cart: EditCart):
    try:
        cart_db = db.query(CartDB).filter(CartDB.id == cart.id).first()
        cart_db.user_id = cart.user_id
        cart_db.product_id = cart.product_id
        cart_db.quantity = cart.quantity
        db.add(cart_db)
        db.commit()
        return cart
    except Exception as e:
        print(e)
        return "something went wrong"


def delete_cart(db: Session, cart: DeleteCart):
    try:
        cart_db = db.query(CartDB).filter(CartDB.id == cart.id).first()
        db.delete(cart_db)
        db.commit()
        return "Cart Deleted"
    except Exception as e:
        print(e)
        return "Something went wrong"


def cart_list(db: Session, cart: ListCart):
    try:
        cart_db = db.query(CartDB).filter(CartDB.user_id == cart.user_id).all()
        return cart_db
    except Exception as e:
        print(e)
        return "Something Went Wrong"
