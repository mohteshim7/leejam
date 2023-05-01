from datetime import datetime
from pydantic.types import constr
from core.config import Base, engine
from sqlalchemy import Boolean, DateTime, Column, String, Integer, ForeignKey, Float, BOOLEAN,JSON

from pydantic import BaseModel


class CreateOrder(BaseModel):
    user_id: constr(strip_whitespace=True)
    product_id: constr(strip_whitespace=True)
    quantity: int
    order_status: constr(strip_whitespace=True)  # (order_received,out_of_delivery,delivered,cancelled)
    price: float
    delivery_status: dict
    payment_status: bool
    payment_method: constr(strip_whitespace=True)


class EditOrder(CreateOrder):
    id: constr(strip_whitespace=True)


class ListOrder(BaseModel):
    user_id: constr(strip_whitespace=True)


class DeleteOrder(BaseModel):
    id: constr(strip_whitespace=True)


class OrderDB(Base):
    __tablename__ = "orders"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(String, index=True, nullable=False, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    product_id = Column(String, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    delivery_status = Column(JSON, nullable=False)
    order_status = Column(String, nullable=False)
    payment_status = Column(BOOLEAN, nullable=False)
    payment_method = Column(String, nullable=False)
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
