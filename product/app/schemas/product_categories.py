from datetime import datetime
from pydantic.types import constr
from core.config import Base, engine
from sqlalchemy import Boolean, DateTime, Column, String

from pydantic import BaseModel


class CreateCategories(BaseModel):
    user_id: constr(strip_whitespace=True)
    name: constr(strip_whitespace=True)


class EditCategories(CreateCategories):
    id: constr(strip_whitespace=True)


class ListCategories(BaseModel):
    user_id: constr(strip_whitespace=True)


class DeleteCategories(BaseModel):
    id: constr(strip_whitespace=True)


class CategoriesDB(Base):
    __tablename__ = "categories"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(String, index=True, nullable=False, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    name = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,

        }


Base.metadata.create_all(engine)
