from pydantic import BaseModel
from datetime import date as date_type, datetime, date

from pydantic.typing import Optional


class StockQuotesCreate(BaseModel):
    date: date_type
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: int
    stock_symbol: str

    class Config:
        orm_mode = True


class StockQuotesShow(BaseModel):
    date: date_type
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    volume: int
    stock_symbol: str

    class Config:
        orm_mode = True
