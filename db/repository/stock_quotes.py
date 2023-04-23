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
                               stock_id=stock_quotes.stock_id)
    db.add(stock_quotes)
    db.commit()
    db.refresh(stock_quotes)
    return stock_quotes
