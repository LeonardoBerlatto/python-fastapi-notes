from fastapi import Depends

from api.config import deps
from api.repository.note_repository import NoteRepository


class NoteService:
    note_repository: NoteRepository

    def __init__(self, note_repository: NoteRepository = Depends(deps.get_note_repository)) -> None:
        super().__init__()
        self.note_repository = note_repository

    def get_notes(self):
        return self.note_repository.get_notes()

    def add_note(self, note):
        return self.note_repository.add_note(note)

    def update_note(self, id, note):
        note_to_update = self.note_repository.get_note_by_id(id)
        note_to_update.title = note.title
        note_to_update.description = note.description
        return self.note_repository.update_note(note_to_update)

    def delete_note(self, id):
        return self.note_repository.delete_note(id)
