from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError

from src.app.auth.permissions import get_user

from src.app.user import models, schemas, service


user_router = APIRouter()


@user_router.get('/me', response_model=schemas.UserPublic)
def user_me(current_user: models.User = Depends(get_user)):
    """ Get user hello there
    """
    if current_user:
        return current_user


@user_router.delete('/delete/{user_id}', response_model=schemas.UserStatus, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    """ Delete user
    """
    deleted_count = await service.user_s.delete(user_id=user_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User with id={user_id} not found")
    return schemas.UserStatus(message=f"Deleted user {user_id}")


@user_router.get('/all', response_model=schemas.UserPublicList)
async def user_list():
    """ Get user
    """
    users = await service.user_s.get_all()
    return {
        "users": users
    }
