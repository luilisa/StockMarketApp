from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.stocks import create_stocks
from schemas.stocks import StocksCreate
from session import get_db

router = APIRouter()


@router.post("/create-stocks")
def post_stocks(stocks: StocksCreate, db: Session = Depends(get_db)):
    stocks = create_stocks(stocks=stocks, db=db)
    return stocks
