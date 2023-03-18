from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
from crud import create_notice, delete_notice, get_notice, get_notices, update_notice
from models import Base
from schemas import NoticeCreate, NoticeUpdate, Notice


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/notices/", response_model=Notice)
async def create_new_notice(notice: NoticeCreate, db: Session = Depends(get_db)):    
    db_notice = create_notice(db, notice)
    return db_notice


@app.get("/notices/", response_model=List[Notice])
async def read_notices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notices = get_notices(db, skip=skip, limit=limit)
    return notices


@app.get("/notices/{notice_id}", response_model=Notice)
async def read_notice(notice_id: int, db: Session = Depends(get_db)):
    db_notice = get_notice(db, notice_id=notice_id)
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    return db_notice


@app.put("/notices/{notice_id}", response_model=Notice)
async def update_notice_by_id(notice_id: int, notice: NoticeUpdate, db: Session = Depends(get_db)):
    db_notice = update_notice(db, notice_id, notice)
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    return db_notice


@app.delete("/notices/{notice_id}", response_model=Notice)
async def delete_notice_by_id(notice_id: int, db: Session = Depends(get_db)):
    db_notice = delete_notice(db, notice_id)
    if db_notice is None:
        raise HTTPException(status_code=404, detail="Notice not found")
    return db_notice
