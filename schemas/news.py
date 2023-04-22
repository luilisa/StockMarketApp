from pydantic import BaseModel
from datetime import date as date_type, datetime, date

from pydantic.typing import Optional


class NewsCreate(BaseModel):
    title: str
    content: str
    pub_date: Optional[date] = datetime.now().date()
    company_id: int

    class Config:
        orm_mode = True


class NewsShow(BaseModel):
    title: str
    content: str
    pub_date: date_type

    class Config:
        orm_mode = True
