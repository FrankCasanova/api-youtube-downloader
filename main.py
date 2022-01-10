from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from dowloader.urls import router
from webapp.urls import web_route


origins = ["http://localhost", "http://localhost:8080", "herokuapp.com"]


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def include_router(app):
    app.include_router(router)
    app.include_router(web_route)


def start_application():
    app = FastAPI()
    include_router(app)
    configure_static(app)
    return app


app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
