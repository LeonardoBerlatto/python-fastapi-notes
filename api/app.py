from fastapi import FastAPI

from api.config.di import init_di
from api.routes import notes_router

app = FastAPI()

app.include_router(notes_router, prefix='/notes', tags=['notes'])
init_di()
