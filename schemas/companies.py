from pydantic import BaseModel
from schemas.news import NewsShow
from schemas.stocks import StocksShow


class CompanyShow(BaseModel):
    company_name: str
    symbol: str
    sector: str
    news: list[NewsShow] = []
    stocks: list[StocksShow] = []

    class Config:
        orm_mode = True


class CompanyCreate(BaseModel):
    company_name: str
    symbol: str
    sector: str

    class Config:
        orm_mode = True

