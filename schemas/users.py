from typing import Optional
from pydantic import BaseModel, EmailStr


# properties required during user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str


class UserShow(BaseModel):
    id: int
    username: str
    email: EmailStr
    hashed_password: str

    class Config:  # to convert non dict obj to json
        orm_mode = True
