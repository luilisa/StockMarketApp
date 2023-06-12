from pydantic import BaseModel

from pydantic.typing import Optional

from schemas.stocks import StocksShow


class StockInPortfolioAdd(BaseModel):
    portfolio_id: id
    stock_id: int

    class Config:
        orm_mode = True


class StockInPortfolioShow(BaseModel):
    portfolio_id: id
    stock_id: int

class Config:
        orm_mode = True