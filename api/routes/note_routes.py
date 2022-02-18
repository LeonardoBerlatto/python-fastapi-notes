from typing import List

from fastapi import APIRouter

from api.models import Note, PydanticObjectId
from api.routes.schemas import UpdateNoteRequest
from api.routes.schemas import NoteRequest
from api.service import NoteService

notes_router = APIRouter()


@notes_router.get("/notes", response_model=List[Note])
def get_notes():
    return NoteService().get_notes()


@notes_router.post("/notes", status_code=201, response_model=Note)
def add_note(note: NoteRequest):
    return NoteService().add_note(note)


@notes_router.put("/notes/{id}", response_model=Note)
def update_note(note_id: PydanticObjectId, note: UpdateNoteRequest):
    return NoteService().update_note(note_id, note)


@notes_router.delete("/notes/{id}", response_model=Note)
def delete_notes(note_id: PydanticObjectId):
    return NoteService().delete_note(note_id)
