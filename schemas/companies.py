from pydantic import BaseModel
from schemas.news import NewsShow


class CompanyShow(BaseModel):
    company_name: str
    symbol: str
    sector: str
    news: list[NewsShow] = []

    class Config:
        orm_mode = True


class CompanyCreate(BaseModel):
    company_name: str
    symbol: str
    sector: str

    class Config:
        orm_mode = True

