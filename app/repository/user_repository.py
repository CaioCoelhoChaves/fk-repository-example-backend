from sqlalchemy.orm import Session
from app.models import User
from app.schema import UserFilterSchema, UserSearchedSchema
from typing import List


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
    def get_by_id(db: Session, user_id: str) -> UserSearchedSchema:
        query = db.query(User).where(User.id == user_id)
        user = query.one()
        return UserSearchedSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            birthday=user.birthday,
            description=user.description,
            created_at=user.created_at
        )
