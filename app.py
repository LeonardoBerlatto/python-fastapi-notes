from fastapi import FastAPI, Depends

from api.config import deps
from api.models.note import Note
from api.repository.note_repository import NoteRepository
from api.schemas.note_request import NoteRequest
from api.schemas.update_note import UpdateNoteRequest
from api.service.note_service import NoteService

app = FastAPI()


@app.get("/notes", response_model=list[Note], tags=['notes'])
def get_notes(note_repository: NoteRepository = Depends(deps.get_note_repository)):
    return NoteService(note_repository).get_notes()


@app.post("/notes", status_code=201, response_model=Note, tags=['notes'])
def add_note(note: NoteRequest,
             note_repository: NoteRepository = Depends(deps.get_note_repository)):
    return NoteService(note_repository).add_note(note)


@app.put("/notes/{id}", response_model=Note, tags=['notes'])
def update_note(note_id: int, note: UpdateNoteRequest,
                note_repository: NoteRepository = Depends(deps.get_note_repository)):
    return NoteService(note_repository).update_note(note_id, note)


@app.delete("/notes/{id}", response_model=Note, tags=['notes'])
def delete_notes(note_id: int,
                 note_repository: NoteRepository = Depends(deps.get_note_repository)):
    return NoteService(note_repository).delete_note(note_id)
