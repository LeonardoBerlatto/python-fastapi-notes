from pydantic import BaseModel


class NoteResponse(BaseModel):
    id: int
    title: str
    description: str
