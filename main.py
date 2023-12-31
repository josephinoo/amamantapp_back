"""
Main module for the FastAPI application.
"""

import os
import sys

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from src.admin.admin import add_views_to_app
from src.config.database import Base, engine, get_session
from src.router import router

engine_db = engine
app = FastAPI(
    dependencies=[Depends(get_session)],
    title="AmamantApp API",
    version="0.1.0",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
app.add_middleware(SessionMiddleware, secret_key="some-random-string")

Base.metadata.create_all(bind=engine_db)


add_views_to_app(app, engine_db)
app.include_router(router, prefix="/api/v1", dependencies=[Depends(get_session)])

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
