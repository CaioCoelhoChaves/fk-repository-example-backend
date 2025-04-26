from pydantic import BaseModel, Field
from datetime import datetime, date
from uuid import UUID
from typing import Optional, Literal


class UserCreateSchema(BaseModel):
    name: str
    email: str
    birthday: date
    description: Optional[str] = None


class UserCreatedSchema(BaseModel):
    id: str


class UserDeletedSchema(BaseModel):
    id: str

class UserSearchedSchema(UserCreateSchema):
    id: UUID
    created_at: datetime



class UserFilterSchema(BaseModel):
    name: str = None
