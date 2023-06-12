from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.typing import List
from sqlalchemy.orm import Session

from db.repository.users import create_new_user, retreive_user, list_users, update_user_by_id, delete_user_by_id
from schemas.users import UserCreate, UserShow
from session import get_db

router = APIRouter()


@router.post("/create-user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=user)
    return user


@router.get("/get/{id}", response_model=UserShow)
def read_user(id: int, db: Session = Depends(get_db)):
    user = retreive_user(id=id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with this id {id} does not exist")
    return user


@router.get("/all", response_model=List[UserShow])
def read_users(db: Session = Depends(get_db)):
    users = list_users(db=db)
    return users


@router.put("/update/{id}")
def update_user(id: int, user: UserCreate, db: Session = Depends(get_db)):
    message = update_user_by_id(id=id, user=user, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
    return {"msg": "Successfully updated data."}


@router.delete("/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    message = delete_user_by_id(id=id, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
    return {"msg": "Successfully deleted."}
