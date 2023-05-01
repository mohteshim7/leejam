from datetime import datetime
from pydantic.types import constr
from core.config import Base, engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy import DateTime, Column, String, JSON, Integer, LargeBinary, ForeignKey

from pydantic import BaseModel


class ProductImage(Base):
    __tablename__ = "products_image"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(String, index=True, nullable=False, primary_key=True)
    product_id = Column(String, ForeignKey('products.id'))
    url = Column(String)


class Product(Base):
    __tablename__ = "products"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(String, index=True, nullable=False, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    product_name = Column(String)
    product_brand_name = Column(String)
    description = Column(String)
    categories = Column(String)
    points = Column(Integer)
    quantity = Column(Integer)
    create_date = Column(DateTime, default=datetime.utcnow)
    images = relationship("ProductImage", backref="product")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_name": self.product_name,
            "product_brand_name": self.product_brand_name,
            "description": self.description,
            "categories": self.categories,
            "points": self.points,
            "quantity": self.quantity,
            "create_date": self.create_date,
        }


class CreateProduct(BaseModel):
    user_id: constr(strip_whitespace=True)
    product_name: constr(strip_whitespace=True)
    product_brand_name: constr(strip_whitespace=True)
    description: constr(strip_whitespace=True)
    categories: constr(strip_whitespace=True)
    points: constr(strip_whitespace=True)
    quantity: int
    quantity: int


class EditProduct(CreateProduct):
    id: constr(strip_whitespace=True)


class EditImage(BaseModel):
    user_id: constr(strip_whitespace=True)
    id: constr(strip_whitespace=True)


class ProductList(BaseModel):
    user_id: constr(strip_whitespace=True)


class DeleteProduct(BaseModel):
    id: constr(strip_whitespace=True)


class GetProduct(BaseModel):
    user_id: constr(strip_whitespace=True)
    id: constr(strip_whitespace=True)


Base.metadata.create_all(engine)
