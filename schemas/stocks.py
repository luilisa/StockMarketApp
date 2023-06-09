from pydantic import BaseModel
from datetime import date as date_type, datetime, date

from pydantic.typing import Optional

from schemas.stocks_quotes import StockQuotesShow


class StocksCreate(BaseModel):
    company_name: str
    stock_price: float
    company_symbol: str

    class Config:
        orm_mode = True


class StocksShow(BaseModel):
    id: int
    company_symbol: str
    company_name: str
    stock_price: float


    class Config:
        orm_mode = True
