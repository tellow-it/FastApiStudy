from fastapi import FastAPI
from core.config import settings
from fastapi.staticfiles import StaticFiles
from db.session import engine
from db.base import Base
from apis.base import api_router


def include_router(application):
    application.include_router(api_router)


def configure_static(application):
    application.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    print('Creating tables...')
    Base.metadata.create_all(bind=engine)
    print('Success create tables!')


def start_application():
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(application)
    configure_static(application)
    create_tables()
    return application


app = start_application()
