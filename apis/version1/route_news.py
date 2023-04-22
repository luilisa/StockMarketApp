from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.typing import List
from sqlalchemy.orm import Session

from db.repository.news import create_news, retreive_news, list_news, update_news_by_id, delete_news_by_id
from schemas.news import NewsCreate, NewsShow
from session import get_db

router = APIRouter()


@router.post("/create-news")
def post_news(news: NewsCreate, db: Session = Depends(get_db)):
    news = create_news(news=news, db=db)
    return news


@router.get("/get/{id}", response_model=NewsShow)
def read_news(id: int, db: Session = Depends(get_db)):
    news = retreive_news(id=id, db=db)
    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"news with this id {id} does not exist")
    return news


@router.get("/all", response_model=List[NewsShow])
def read_news(db: Session = Depends(get_db)):
    news = list_news(db=db)
    return news


@router.put("/update/{id}")
def update_news(id: int, news: NewsCreate, db: Session = Depends(get_db)):
    message = update_news_by_id(id=id, news=news, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"news with id {id} not found")
    return {"msg": "Successfully updated data."}


@router.delete("/delete/{id}")
def delete_news(id: int, db: Session = Depends(get_db)):
    message = delete_news_by_id(id=id, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"news with id {id} not found")
    return {"msg": "Successfully deleted."}