from pydantic import BaseModel, Field
from datetime import datetime, date
from uuid import UUID
from typing import Optional, Literal


class UserSchemaBase(BaseModel):
    id: UUID
    name: str
    email: str
    birthday: date
    description: Optional[str] = None
    created_at: datetime


class UserCreateSchema(UserSchemaBase):
    created_at: Literal[None] = None


class UserSearchedSchema(UserSchemaBase):
    pass


class UserFilterSchema(BaseModel):
    name: str = None
