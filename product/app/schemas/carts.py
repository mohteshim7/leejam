from datetime import datetime
from pydantic.types import constr
from core.config import Base, engine
from sqlalchemy import Boolean, DateTime, Column, String, Integer, ForeignKey

from pydantic import BaseModel


class CreateCart(BaseModel):
    user_id: constr(strip_whitespace=True)
    product_id: constr(strip_whitespace=True)
    quantity: int


class EditCart(CreateCart):
    id: constr(strip_whitespace=True)


class ListCart(BaseModel):
    user_id: constr(strip_whitespace=True)


class DeleteCart(BaseModel):
    id: constr(strip_whitespace=True)


class CartDB(Base):
    __tablename__ = "carts"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(String, index=True, nullable=False, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    product_id = Column(String, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "create_date": self.create_date,
        }


Base.metadata.create_all(engine)
