from pydantic.typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.repository.stocks import create_stocks, retreive_stock, list_stocks, delete_stock_by_id, update_stock_by_id
from schemas.stocks import StocksCreate, StocksShow
from session import get_db

router = APIRouter()


@router.post("/create-stocks")
def post_stocks(stocks: StocksCreate, db: Session = Depends(get_db)):
    stocks = create_stocks(stocks=stocks, db=db)
    return stocks

@router.get("/get/{id}", response_model=StocksShow)
def read_stock(id: int, db: Session = Depends(get_db)):
    stock = retreive_stock(id=id, db=db)
    if not stock:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"stock with this id {id} does not exist")
    return stock


@router.get("", response_model=List[StocksShow])
def read_stocks(db: Session = Depends(get_db)):
    stocks = list_stocks(db=db)
    return stocks

# @router.get("/get/{company_symbol}", response_model=StockQuotesShow)
# def read_stock_quotes(company_symbol: str, db: Session = Depends(get_db)):
#     get_stock_quotes = list_stocks(db=db)
#     return stocks


@router.put("/update/{id}")
def update_stock(id: int, stock: StocksCreate, db: Session = Depends(get_db)):
    message = update_stock_by_id(id=id, stock=stock, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stock with id {id} not found")
    return {"msg": "Successfully updated data."}


@router.delete("/delete/{id}")
def delete_stock(id: int, db: Session = Depends(get_db)):
    message = delete_stock_by_id(id=id, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stock with id {id} not found")
    return {"msg": "Successfully deleted."}