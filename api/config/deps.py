from api.repository.note_repository import NoteRepository
from api.service.note_service import NoteService


def get_note_repository():
    return NoteRepository()

def get_note_service():
    return NoteService()