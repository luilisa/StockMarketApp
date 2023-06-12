from datetime import datetime
from pydantic.typing import List
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


def create_list_stock_quotes(db: Session, stock_quotes: List[StockQuotesCreate]):
    db.query(StockQuotes).delete()
    for stock_quote in stock_quotes:
        stock_quote = StockQuotes(date=stock_quote["TRADEDATE"],
                                  open_price=stock_quote["OPEN"],
                                  high_price=stock_quote["HIGH"],
                                  low_price=stock_quote["LOW"],
                                  close_price=stock_quote["CLOSE"],
                                  volume=stock_quote["VOLUME"],
                                  stock_symbol=stock_quote["SECID"])
        db.add(stock_quote)
    db.commit()

    return stock_quotes


def list_stock_quotes(db: Session):
    stock_quotes = db.query(StockQuotes).all()
    return stock_quotes


def retreive_stock_quotes(company_symbol: str, db: Session):
    item = db.query(StockQuotes).filter(StockQuotes.stock_symbol == company_symbol).all()
    return item
