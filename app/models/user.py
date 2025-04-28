from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, UUID, DateTime, Date, text
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, server_default=text("gen_random_uuid()"))
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now(), server_default=text("CURRENT_TIMESTAMP"))
