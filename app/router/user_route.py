from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from app.database import get_db
from app.exceptions import not_found_exception
from app.exceptions.exceptions import not_found_exception_doc
from app.repository import UserRepository
from app.schema import UserSearchedSchema, UserFilterSchema
from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Annotated, List
from loguru import logger

router = APIRouter(prefix="/users")


@router.get("", response_model=List[UserSearchedSchema], status_code=200)
async def find(filter_query: Annotated[UserFilterSchema, Query()], db: Session = Depends(get_db)):
    try:
        logger.debug(f"Trying to find user: {filter_query}")
        return UserRepository.find(db, filter_query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"error: {e}")

get_by_id_responses = {}
get_by_id_responses.update(not_found_exception_doc)


@router.get("/{user_id}", response_model=UserSearchedSchema, status_code=200, responses=get_by_id_responses)
async def get_by_id(user_id: str, db: Session = Depends(get_db)):
    try:
        logger.debug(f"Trying to find user by id: {user_id}")
        return UserRepository.get_by_id(db, user_id)
    except NoResultFound:
        raise not_found_exception
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Not expected error: {e}")
