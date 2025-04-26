from sqlalchemy import ColumnElement
from sqlalchemy.orm import Session
from app.models import User
from app.schema import UserFilterSchema, UserSearchedSchema, UserCreateSchema, UserCreatedSchema, UserDeletedSchema
from typing import List, cast


class UserRepository:

    @staticmethod
    def find(db: Session, user_query: UserFilterSchema) -> List[UserSearchedSchema]:
        query = db.query(User)
        if user_query.name is not None:
            query = query.where(User.name.ilike(f"%{user_query.name}%"))

        users = query.all()
        response = []

        for user in users:
            response.append(
                UserSearchedSchema(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    birthday=user.birthday,
                    description=user.description,
                    created_at=user.created_at
                )
            )

        return response


    @staticmethod
    def create(db: Session, user: UserCreateSchema) -> UserCreatedSchema:
        new_user = User(
            name=user.name,
            email=user.email,
            birthday=user.birthday,
            description=user.description
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserCreatedSchema(id=str(new_user.id))


    @staticmethod
    def get_by_id(db: Session, user_id: str) -> UserSearchedSchema:
        query = db.query(User).where(cast(ColumnElement[bool], User.id == user_id))
        user = query.one()
        return UserSearchedSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            birthday=user.birthday,
            description=user.description,
            created_at=user.created_at
        )

    @staticmethod
    def delete(db: Session, user_id: str) -> UserDeletedSchema:
        db.query(User).where(cast(ColumnElement[bool], User.id == user_id)).delete()
        db.commit()
        return UserDeletedSchema(id=user_id)
