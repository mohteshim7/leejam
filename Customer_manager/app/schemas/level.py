from datetime import datetime
from pydantic.types import constr
from core.config import Base, engine
from sqlalchemy import DateTime, Column, String, JSON

from pydantic import BaseModel


class CreateLevel(BaseModel):
    user_id: constr(strip_whitespace=True)
    reason: constr(strip_whitespace=True)
    level: constr(strip_whitespace=True)


class EditLevel(CreateLevel):
    id: constr(strip_whitespace=True)

class GetLevel(BaseModel):
    user_id: constr(strip_whitespace=True)

class CustomerLevel(Base):
    __tablename__ = "customer_level"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(String, index=True, nullable=False, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    reason = Column(String)
    level = Column(JSON)
    create_date = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "reason": self.reason,
            "level": self.level,
            "create_date": self.create_date,
        }


Base.metadata.create_all(engine)
