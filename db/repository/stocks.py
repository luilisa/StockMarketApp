from datetime import datetime

from sqlalchemy.orm import Session

from db.models.stocks import Stocks
from schemas.stocks import StocksCreate


def create_stocks(db: Session, stocks: StocksCreate):
    stocks = Stocks(company_name=stocks.company_name,
                    stock_price=stocks.stock_price,
                    company_symbol=stocks.company_symbol)
    db.add(stocks)
    db.commit()
    db.refresh(stocks)
    return stocks


def retreive_stock(id: int, db: Session):
    item = db.query(Stocks).filter(Stocks.id == id).first()
    return item


def list_stocks(db: Session):
    stocks = db.query(Stocks).all()
    return stocks


def update_stock_by_id(id: int, stock: StocksCreate, db: Session):
    existing_stock = db.query(Stocks).filter(Stocks.id == id)
    if not existing_stock.first():
        return 0
    existing_stock.update(stock.__dict__)
    db.commit()
    return 1


def delete_stock_by_id(id: int, db: Session):
    existing_stock = db.query(Stocks).filter(Stocks.id == id)
    if not existing_stock.first():
        return 0
    existing_stock.delete(synchronize_session=False)
    db.commit()
    return 1
