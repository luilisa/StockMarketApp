from datetime import datetime

from sqlalchemy.orm import Session
from pydantic.typing import List
from db.models.news import News
from moex.client import get_news_by_id
from schemas.news import NewsCreate


def create_news(db: Session, news: NewsCreate):
    news = News(title=news.title,
                pub_date=news.pub_date,
                link = news.link)
    db.add(news)
    db.commit()
    db.refresh(news)
    return news

def create_list_news(db: Session, news: List[NewsCreate]):
    db.query(News).delete()
    url = 'https://moex.com/n{id}'
    for new in news:
        new = News(title=new["title"],
                   pub_date=new["published_at"],
                   link=url.format(id=new["id"]))
        db.add(new)
    db.commit()

    return news
def retreive_news(id: int, db: Session):
    item = get_news_by_id(id)
    news = item['body']
    return news


def list_news(db: Session):
    news = db.query(News).all()  #filter(News.pub_date == datetime.now().date())
    return news


def update_news_by_id(id: int, news: NewsCreate, db: Session):
    existing_news = db.query(News).filter(News.id == id)
    if not existing_news.first():
        return 0
    existing_news.update(news.__dict__)
    db.commit()
    return 1


def delete_news_by_id(id: int, db: Session):
    existing_news = db.query(News).filter(News.id == id)
    if not existing_news.first():
        return 0
    existing_news.delete(synchronize_session=False)
    db.commit()
    return 1