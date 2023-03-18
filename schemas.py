from datetime import datetime
from pydantic import BaseModel, validator

class NoticeBase(BaseModel):
    title: str
    content: str
    email: str

    @validator('email')
    def email_valid(cls, v):
        if '@' not in v:           
            raise ValueError('Invalid email')
        return v

class NoticeCreate(NoticeBase):
    pass

class NoticeUpdate(NoticeBase):
    pass

class Notice(NoticeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
