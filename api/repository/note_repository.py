import abc

from api.models import Note


class NoteRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_notes(self):
        pass

    @abc.abstractmethod
    def get_note_by_id(self, note_id: int):
        pass

    @abc.abstractmethod
    def add_note(self, note: Note):
        pass

    @abc.abstractmethod
    def update_note(self, note_to_update: Note):
        pass

    @abc.abstractmethod
    def delete_note(self, note_id: int):
        pass
