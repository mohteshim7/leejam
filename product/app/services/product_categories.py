import pdb
import uuid
from sqlalchemy import exc
from app.schemas.product_categories import CategoriesDB, CreateCategories, DeleteCategories, EditCategories, \
    ListCategories
from sqlalchemy.orm import Session


def new_category_id(db):
    while True:
        id = str(uuid.uuid4())
        data = db.query(CategoriesDB).filter(CategoriesDB.id == id).first()
        if not data:
            return id


def create_categories(db: Session, user: CreateCategories):
    try:
        pdb.set_trace()
        id = new_category_id(db)
        pc = CategoriesDB(
            id=id,
            user_id=user.user_id,
            name=user.name,
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


def edit_categories(db: Session, category: EditCategories):
    try:
        categories_db = db.query(CategoriesDB).filter(CategoriesDB.id == category.id).first()
        categories_db.user_id = category.user_id
        categories_db.name = category.name
        db.add(categories_db)
        db.commit()
        return category
    except Exception as e:
        print(e)
        return "something went wrong"


def delete_categories(db: Session, category: DeleteCategories):
    try:
        categories_db = db.query(CategoriesDB).filter(CategoriesDB.id == category.id).first()
        db.delete(categories_db)
        db.commit()
        return "Category Deleted"
    except Exception as e:
        print(e)
        return "Something went wrong"


def category_list(db: Session, category: ListCategories):
    try:
        categories_db = db.query(CategoriesDB).filter(CategoriesDB.user_id == category.user_id).all()
        return categories_db
    except Exception as e:
        print(e)
        return "Something Went Wrong"
