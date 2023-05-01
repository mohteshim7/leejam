import uuid
from sqlalchemy import exc
from app.schemas import EditLevel, CreateLevel, CustomerLevel, GetLevel
from sqlalchemy.orm import Session


def new_level_id(db):
    while True:
        id = str(uuid.uuid4())
        data = db.query(CustomerLevel).filter(CustomerLevel.id == id).first()
        if not data:
            return id


def create_levels(db: Session, user: CreateLevel):
    try:
        id = new_level_id(db)
        ld = CustomerLevel(
            id=id,
            user_id=user.user_id,
            reason=user.reason,
            level=user.level
        )
        db.add(ld)
        db.commit()
        db.refresh(ld)
        return ld.to_dict()
    except exc.IntegrityError as e:
        print(e)
        return "User Exist"
    except Exception as e:
        print(e)
        return "something went wrong"


def edit_levels(db: Session, level: EditLevel):
    try:
        level_db = db.query(CustomerLevel).filter(CustomerLevel.id ==level.id).first()
        level_db.user_id = level.user_id
        level_db.reason = level.reason
        level_db.level = level.level
        db.add(level_db)
        db.commit()
        return f"level {level.id} updated successfully"
    except Exception as e:
        print(e)
        return "something went wrong"


def get_levels(db: Session, level: GetLevel):
    level_db = db.query(CustomerLevel).filter(CustomerLevel.user_id == level.user_id).all()

    return level_db
