from datetime import datetime

from sqlalchemy.orm import Session

from db.models.stock_quotes import StockQuotes
from schemas.stocks_quotes import StockQuotesCreate


def create_stock_quotes(db: Session, stock_quotes: StockQuotesCreate):
    stock_quotes = StockQuotes(date=stock_quotes.date,
                               open_price=stock_quotes.open_price,
                               high_price=stock_quotes.high_price,
                               low_price=stock_quotes.low_price,
                               close_price=stock_quotes.close_price,
                               volume=stock_quotes.volume,
                               stock_symbol=stock_quotes.stock_symbol)
    db.add(stock_quotes)
    db.commit()
    db.refresh(stock_quotes)
    return stock_quotes


def list_stock_quotes(db: Session):
    stock_quotes = db.query(StockQuotes).all()
    return stock_quotes


def retreive_stock_quotes(company_symbol: str, db: Session):
    item = db.query(StockQuotes).filter(StockQuotes.stock_symbol == company_symbol).first()
    return item
