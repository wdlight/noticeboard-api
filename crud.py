from sqlalchemy.orm import Session
from models import Notice
from schemas import NoticeCreate, NoticeUpdate


def get_notice(db: Session, notice_id: int):
    return db.query(Notice).filter(Notice.id == notice_id).first()


def get_notices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notice).offset(skip).limit(limit).all()


def create_notice(db: Session, notice: NoticeCreate):
    db_notice = Notice(**notice.dict())
    print ( ">>>>>>>>>>>>>>11")
    db.add(db_notice)
    print ( ">>>>>>>>>>>>>>22")
    db.commit()
    db.refresh(db_notice)
    return db_notice


def update_notice(db: Session, notice_id: int, notice: NoticeUpdate):
    db_notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if db_notice:
        for key, value in notice.dict(exclude_unset=True).items():
            setattr(db_notice, key, value)
        db.commit()
        db.refresh(db_notice)
        return db_notice


def delete_notice(db: Session, notice_id: int):
    db_notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if db_notice:
        db.delete(db_notice)
        db.commit()
        return db_notice
