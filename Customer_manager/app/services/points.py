import pdb
import uuid
from sqlalchemy import exc
from app.schemas.points import PointsDB, CreatePoint, CancelPoint, EditPoint,ListPoint
from sqlalchemy.orm import Session


def new_point_id(db):
    while True:
        id = str(uuid.uuid4())
        data = db.query(PointsDB).filter(PointsDB.id == id).first()
        if not data:
            return id


def create_points(db: Session, user: CreatePoint):
    try:
        pdb.set_trace()
        id = new_point_id(db)
        pc = PointsDB(
            id=id,
            user_id=user.user_id,
            created_reason=user.created_reason,
            expire_date=user.expire_date
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


def edit_points(db: Session, point: EditPoint):
    try:
        point_db = db.query(PointsDB).filter(PointsDB.id==point.id).first()
        point_db.user_id = point.user_id
        point_db.created_reason = point.created_reason
        point_db.expire_date = point.expire_date
        db.add(point_db)
        db.commit()
        return point
    except Exception as e:
        print(e)
        return "something went wrong"


def cancel_points(db: Session, point: CancelPoint):
    try:
        point_db = db.query(PointsDB).filter(PointsDB.id==point.id).first()
        point_db.rejected_reason = point.rejected_reason
        point_db.rejected = point.rejected
        db.add(point_db)
        db.commit()
        return "Point Canceled"
    except Exception as e:
        print(e)
        return "Something went wrong"

def point_list(db: Session, point: ListPoint):
    try:
        point_db = db.query(PointsDB).filter(PointsDB.user_id == point.user_id).all()
        return point_db
    except Exception as e:
        print(e)
        return "Something Went Wrong"
