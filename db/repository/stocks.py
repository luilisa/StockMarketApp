from datetime import datetime

from sqlalchemy.orm import Session

from db.models.stocks import Stocks
from schemas.stocks import StocksCreate


def create_stocks(db: Session, stocks: StocksCreate):
    stocks = Stocks(figi=stocks.figi,
                    stock_price=stocks.stock_price,
                    company_symbol=stocks.company_symbol)
    db.add(stocks)
    db.commit()
    db.refresh(stocks)
    return stocks
