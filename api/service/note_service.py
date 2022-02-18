from pythondi import inject

from api.models.note import Note
from api.repository.note_repository import NoteRepository
from api.routes.schemas.note_request import NoteRequest


class NoteService:
    note_repository: NoteRepository

    @inject()
    def __init__(self, note_repository: NoteRepository):
        self.note_repository = note_repository
        pass

    def get_notes(self):
        return self.note_repository.get_notes()

    def add_note(self, note: NoteRequest):
        return self.note_repository.add_note(Note.construct(title=note.title, description=note.description))

    def update_note(self, id, note):
        note_to_update = Note.parse_obj(self.note_repository.get_note_by_id(id))
        note_to_update.title = note.title
        note_to_update.description = note.description
        return self.note_repository.update_note(note_to_update)

    def delete_note(self, id):
        return self.note_repository.delete_note(id)
