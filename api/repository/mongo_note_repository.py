from bson import ObjectId

from api.config import database
from api.models.note import Note
from api.repository.note_repository import NoteRepository

COLLECTION_NAME = 'notes'


class MongoNoteRepository(NoteRepository):

    def __init__(self) -> None:
        super().__init__()

    def get_notes(self):
        return list(database[COLLECTION_NAME].find())

    def get_note_by_id(self, note_id: int):
        return database[COLLECTION_NAME].find_one({'_id': ObjectId(note_id)})

    def add_note(self, note: Note):
        id = database[COLLECTION_NAME].insert_one(dict(note)).inserted_id
        note.id = id
        return note

    def update_note(self, note_to_update: Note):
        return database[COLLECTION_NAME].find_one_and_update({'_id': ObjectId(note_to_update.id)},
                                                             {'$set': dict(note_to_update)},
                                                             return_document=True)

    def delete_note(self, note_id: int):
        return database[COLLECTION_NAME].find_one_and_delete({'_id': ObjectId(note_id)})
