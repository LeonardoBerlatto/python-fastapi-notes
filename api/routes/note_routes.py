from fastapi import APIRouter, Depends

from api.config import deps
from api.models.note import Note
from api.repository.note_repository import NoteRepository
from api.routes.schemas.note_request import NoteRequest
from api.routes.schemas import UpdateNoteRequest
from api.service.note_service import NoteService

notes_router = APIRouter()


@notes_router.get("/notes", response_model=list[Note])
def get_notes(note_repository: NoteRepository = Depends(deps.get_note_repository)):
    return NoteService(note_repository).get_notes()


@notes_router.post("/notes", status_code=201, response_model=Note)
def add_note(note: NoteRequest,
             note_repository: NoteRepository = Depends(deps.get_note_repository)):
    return NoteService(note_repository).add_note(note)


@notes_router.put("/notes/{id}", response_model=Note)
def update_note(note_id: int, note: UpdateNoteRequest,
                note_repository: NoteRepository = Depends(deps.get_note_repository)):
    return NoteService(note_repository).update_note(note_id, note)


@notes_router.delete("/notes/{id}", response_model=Note)
def delete_notes(note_id: int,
                 note_repository: NoteRepository = Depends(deps.get_note_repository)):
    return NoteService(note_repository).delete_note(note_id)
