from pydantic import BaseModel
from datetime import date as date_type, datetime, date

from pydantic.typing import Optional, List

from schemas.stocks import StocksShow


class PortfolioCreate(BaseModel):
    # id: str
    portfolio_name: str
    owner_email: str
    # stocks: List[StocksShow]

    class Config:
        orm_mode = True


class PortfolioShow(BaseModel):
    id: str
    portfolio_name: str
    owner_email: str
    stocks: List[StocksShow]

    class Config:
        orm_mode = True


class PortfolioSchema(PortfolioCreate):
    stocks: List[StocksShow]
