from datetime import datetime
import pytz
from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Notice(Base):
    __tablename__ = "notices"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now(pytz.timezone("Asia/Seoul")), index=True)
    updated_at = Column(DateTime, default=datetime.now(pytz.timezone("Asia/Seoul")), onupdate=datetime.now(pytz.timezone("Asia/Seoul")), index=True)
    email = Column(String, index=True)
