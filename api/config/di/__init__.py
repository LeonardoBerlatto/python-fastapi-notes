from pythondi import Provider, configure

from api.repository.mongo_note_repository import NoteRepository, MongoNoteRepository


def init_di():
    provider = Provider()
    provider.bind(NoteRepository, MongoNoteRepository)
    configure(provider=provider)
