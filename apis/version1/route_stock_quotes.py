from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.stock_quotes import create_stock_quotes
from schemas.stocks_quotes import StockQuotesCreate
from session import get_db

router = APIRouter()


@router.post("/create-quotes")
def post_stocks_quotes(stock_quotes: StockQuotesCreate, db: Session = Depends(get_db)):
    stock_quotes = create_stock_quotes(stock_quotes=stock_quotes, db=db)
    return stock_quotes
