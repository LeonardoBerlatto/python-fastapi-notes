from typing import Optional

from pydantic import BaseModel


class UpdateNoteRequest(BaseModel):
    title: Optional[str]
    description: Optional[str]
