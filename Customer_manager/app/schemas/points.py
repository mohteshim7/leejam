from datetime import datetime
from pydantic.types import constr
from core.config import Base, engine
from sqlalchemy import Boolean, DateTime, Column, String

from pydantic import BaseModel


class CreatePoint(BaseModel):
    user_id: constr(strip_whitespace=True)
    created_reason: constr(strip_whitespace=True)
    expire_date: datetime


class EditPoint(CreatePoint):
    id: constr(strip_whitespace=True)

class ListPoint(BaseModel):
    user_id: constr(strip_whitespace=True)

class CancelPoint(BaseModel):
    id: constr(strip_whitespace=True)
    rejected_reason: constr(strip_whitespace=True)
    rejected: bool


class PointsDB(Base):
    __tablename__ = "points"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(String, index=True, nullable=False, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    created_reason = Column(String)
    rejected_reason = Column(String, default=None)
    rejected = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    expire_date = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "created_reason": self.created_reason,
            "rejected_reason": self.rejected_reason,
            "rejected": self.rejected,
            "create_date": self.create_date,
            "expire_date": self.expire_date,
        }


Base.metadata.create_all(engine)
