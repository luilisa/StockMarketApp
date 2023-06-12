from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.typing import List
from sqlalchemy.orm import Session

from db.repository.portfolios import create_portfolio, list_portfolios, retreive_portfolio, put_stock_to_portfolio, \
    get_portfolio,  delete_stock
from db.repository.stock_quotes import create_stock_quotes, list_stock_quotes, retreive_stock_quotes, \
    create_list_stock_quotes
from schemas.portfolios import PortfolioCreate, PortfolioShow
from schemas.stocks_quotes import StockQuotesCreate, StockQuotesShow
from session import get_db
from moex.client import get_stock_history_by_ticker

router = APIRouter()


@router.post("/create-portfolio")
def post_portfolio(portfolio: PortfolioCreate, db: Session = Depends(get_db)):
    portfolio = create_portfolio(portfolio=portfolio, db=db)
    return portfolio


@router.get("/", response_model=List[PortfolioShow])
def read_portfolios(db: Session = Depends(get_db)):
    portfolios = list_portfolios(db=db)
    return portfolios


@router.get("/owner={owner_email}", response_model=List[PortfolioShow])
def read_portfolios(owner_email: str, db: Session = Depends(get_db)):
    portfolios = retreive_portfolio(owner_email=owner_email, db=db)
    if not portfolios:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"portfolio with this owner_email {owner_email} does not exist")
    return portfolios


@router.get("/{portfolio_id}", response_model=PortfolioShow)
def read_portfolios_by_id(portfolio_id: int, db: Session = Depends(get_db)):
    portfolio = get_portfolio(portfolio_id=portfolio_id, db=db)
    if not portfolio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"portfolio with this id {id} does not exist")
    return portfolio


@router.put("/update/{portfolio_id}/stocks/{stock_id}")
def update_portfolio(stock_id: int, portfolio_id: int, db: Session = Depends(get_db)):
    message = put_stock_to_portfolio(portfolio_id=portfolio_id, stock_id=stock_id, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stock with id {id} not found")
    return message


@router.delete("/delete/{portfolio_id}/stocks/{stock_id}")
def delete_stock_in_portfolio(portfolio_id: int, stock_id: int, db: Session = Depends(get_db)):
    message = delete_stock(portfolio_id=portfolio_id, stock_id=stock_id, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stock_id with id {stock_id} not found in portfolio")
    return {"msg": "Successfully deleted."}