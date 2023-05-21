from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.typing import List
from sqlalchemy.orm import Session

from db.repository.stock_quotes import create_stock_quotes, list_stock_quotes, retreive_stock_quotes
from schemas.stocks_quotes import StockQuotesCreate, StockQuotesShow
from session import get_db

router = APIRouter()


@router.post("/create-quotes")
def post_stocks_quotes(stock_quotes: StockQuotesCreate, db: Session = Depends(get_db)):
    stock_quotes = create_stock_quotes(stock_quotes=stock_quotes, db=db)
    return stock_quotes


@router.get("/all", response_model=List[StockQuotesShow])
def read_stocks(db: Session = Depends(get_db)):
    stocks_quotes = list_stock_quotes(db=db)
    return stocks_quotes


@router.get("/{company_symbol}", response_model=StockQuotesShow)
def read_stock_quotes(company_symbol: str, db: Session = Depends(get_db)):
    stocks_quotes = retreive_stock_quotes(company_symbol=company_symbol, db=db)
    if not stocks_quotes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stocks quotes with this symbol {company_symbol} does not exist")
    return stocks_quotes
