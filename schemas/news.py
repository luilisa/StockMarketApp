from pydantic import BaseModel
from datetime import date as date_type, datetime, date

from pydantic.typing import Optional


class NewsCreate(BaseModel):
    id: int
    link: str
    title: str
    pub_date: Optional[date]

    class Config:
        orm_mode = True


class NewsShow(BaseModel):
    id: int
    link: str
    title: str
    pub_date: date_type

    class Config:
        orm_mode = True
