from api.models.note import Note


class NoteRepository:
    notes: list[Note] = []

    def get_notes(self):
        return self.notes

    def get_note_by_id(self, note_id: int):
        return self.notes[note_id - 1]

    def add_note(self, note: Note):
        note.id = len(self.notes) + 1
        return self.notes.append(note)

    def update_note(self, note_to_update: Note):
        self.notes[note_to_update.id - 1] = note_to_update

    def delete_note(self, note_id: int):
        self.notes.pop(note_id - 1)
