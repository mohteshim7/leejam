import os
import pdb
import uuid
import shutil
from sqlalchemy import exc
from app.schemas import CreateProduct, EditProduct, EditImage, GetProduct, ProductList, DeleteProduct, Product, \
    ProductImage
from sqlalchemy.orm import Session


def new_product_id(db):
    while True:
        id = str(uuid.uuid4())
        data = db.query(Product).filter(Product.id == id).first()
        if not data:
            return id


def new_product_image_id(db):
    while True:
        id = str(uuid.uuid4())
        data = db.query(ProductImage).filter(ProductImage.id == id).first()
        if not data:
            return id


def create_product(db: Session, product: CreateProduct, files):
    try:
        pdb.set_trace()
        id = new_product_id(db)
        pd = Product(
            id=id,
            user_id=product.user_id,
            product_name=product.product_name,
            product_brand_name=product.product_brand_name,
            description=product.description,
            categories=product.categories,
            points=int(product.points),
            quantity=int(product.quantity),
        )
        db.add(pd)
        db.commit()
        db.refresh(pd)
        for image in files:
            image_uuid = new_product_image_id(db)
            image_path = os.path.join("static/product_images", image_uuid + ".jpg")
            with open(image_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            db_image = ProductImage(
                id=image_uuid,
                product_id=id,
                url=image_path)
            db.add(db_image)
            db.commit()
            db.refresh(db_image)
        return pd.to_dict()
    except exc.IntegrityError as e:
        print(e)
        return "User Exist"
    except Exception as e:
        print(e)
        return "something went wrong"


def edit_product(db: Session, product: EditProduct):
    try:
        product_db = db.query(Product).filter(Product.id == product.id).first()
        product_db.user_id = product.user_id
        product_db.product_name = product.product_name
        product_db.product_brand_name = product.product_brand_name
        product_db.description = product.description
        product_db.categories = product.categories
        product_db.points = product.points
        product_db.quantity = product.quantity
        db.add(product_db)
        db.commit()
        return f"level {product.product_name} updated successfully"
    except Exception as e:
        print(e)
        return "something went wrong"


def get_product(db: Session, product: GetProduct):
    prod_db = db.query(Product).filter(Product.id == product.id).first()

    return prod_db


def list_product(db: Session, prod: ProductList):
    prod_db = db.query(Product).filter(Product.user_id == prod.user_id).all()
    return prod_db


def delete_product(db: Session, prod: DeleteProduct):
    prod_img_db = db.query(ProductImage).filter(ProductImage.product_id == prod.id).all()
    for img in prod_img_db:
        url = img.url
        os.remove(url)
        db.delete(prod_img_db)
        db.commit()
    prod_db = db.query(Product).filter(Product.id == prod.id).first()
    name = prod_db.product_name
    db.delete(prod_db)
    db.commit()

    return f" deleted"
