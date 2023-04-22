from sqlalchemy.orm import Session

from db.models.users import Users
from schemas.users import UserCreate


def create_new_user(db: Session, user: UserCreate):
    user = Users(username=user.username,
                 email=user.email,
                 hashed_password=user.hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def retreive_user(id: int, db: Session):
    item = db.query(Users).filter(Users.id == id).first()
    return item


def list_users(db: Session):
    users = db.query(Users).all()  # filter(News.pub_date == datetime.now().date())
    return users


def update_user_by_id(id: int, user: UserCreate, db: Session):
    existing_user = db.query(Users).filter(Users.id == id)
    if not existing_user.first():
        return 0
    existing_user.update(user.__dict__)
    db.commit()
    return 1


def delete_user_by_id(id: int, db: Session):
    existing_user = db.query(Users).filter(Users.id == id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1
