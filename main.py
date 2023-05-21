from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from apis.base import api_router
# from apis.base import api_router
from config import settings
from db.repository.users import create_new_user
from schemas.users import UserCreate
# from apis.general_pages.route_homepage import general_pages_router
from session import engine, get_db  # new
from db.base import Base  # new


def include_router(app):
    app.include_router(api_router)


# def configure_static(app):
#     app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():  # new
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    origins = [
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app)
    # configure_static(app)
    create_tables()  # new
    return app


app = start_application()

#
# @app.post("/")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     user = create_new_user(user=user, db=db)
#     return user
