from datetime import datetime

from sqlalchemy.orm import Session

from db.models.news import News
from schemas.news import NewsCreate


def create_news(db: Session, news: NewsCreate):
    news = News(title=news.title,
                content=news.content,
                pub_date=news.pub_date,
                company_id=news.company_id)
    db.add(news)
    db.commit()
    db.refresh(news)
    return news


def retreive_news(id: int, db: Session):
    item = db.query(News).filter(News.id == id).first()
    return item


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