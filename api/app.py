from fastapi import FastAPI

from api.routes import notes_router

app = FastAPI()

app.include_router(notes_router, prefix='/notes', tags=['notes'])
