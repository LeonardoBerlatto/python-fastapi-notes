from api.repository.mongo_note_repository import NoteRepository


def get_note_repository():
    return NoteRepository()
