from pydantic import BaseModel, Field

from api.models.base_object_id import PydanticObjectId


class Note(BaseModel):
    id: PydanticObjectId = Field(..., alias='_id')
    title: str
    description: str