from datetime import datetime
from pydantic.typing import List
from sqlalchemy.orm import Session, joinedload

from db.models.portfolios import Portfolios
from db.models.stocks import Stocks
from db.models.stocks_in_portfolio import StocksInPortfolio
from db.repository.stocks import retreive_stock
from schemas.portfolios import PortfolioCreate


def create_portfolio(db: Session, portfolio: PortfolioCreate):
    portfolio = Portfolios(portfolio_name=portfolio.portfolio_name,
                               owner_email=portfolio.owner_email)

    db.add(portfolio)
    db.commit()
    db.refresh(portfolio)
    return portfolio


def list_portfolios(db: Session):
    portfolios = db.query(Portfolios).options(joinedload(Portfolios.stocks)).all()
    return portfolios


def retreive_portfolio(owner_email: str, db: Session):
    item = db.query(Portfolios).filter(Portfolios.owner_email == owner_email).all()
    return item


def get_portfolio(portfolio_id: int, db: Session):
    item = db.query(Portfolios).filter(Portfolios.id == portfolio_id).first()

    return item


def put_stock_to_portfolio(stock_id: int, portfolio_id: int, db: Session):
    existing_stock = retreive_stock(stock_id, db=db)
    existing_portfolio = get_portfolio(portfolio_id, db=db)
    stocksinportfolio = StocksInPortfolio(stock_id= existing_stock.id,
                                          portfolio_id= existing_portfolio.id)
    db.add(stocksinportfolio)
    db.commit()
    portfolio = db.query(Portfolios).filter(Portfolios.id == portfolio_id).first()

    return portfolio


def delete_stock(portfolio_id: int, stock_id: int, db: Session):
    existing_stock = retreive_stock(stock_id, db=db)
    existing_portfolio = get_portfolio(portfolio_id, db=db)
    db.query(StocksInPortfolio).filter_by(portfolio_id=existing_portfolio.id,
                                          stock_id=existing_stock.id).delete(synchronize_session=False)


    db.commit()
    return 1