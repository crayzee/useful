from typing import List

from fastapi import APIRouter, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError

from src.app.auth.permissions import get_user, get_superuser

from src.app.user import models, schemas, service


admin_router = APIRouter()


@admin_router.get('', response_model=List[service.user_s.get_schema])
async def get_all_users(user: models.User = Depends(get_superuser)):
    """ Get all users
    """
    return await service.user_s.all()


@admin_router.get('/{pk}', response_model=schemas.UserInDB)
async def get_single_user(pk: int, user: models.User = Depends(get_superuser)):
    """ Get user """
    return await service.user_s.get(id=pk)


@admin_router.post('', response_model=schemas.UserInDB)
async def create_user(schema: schemas.UserCreate, user: models.User = Depends(get_superuser)):
    """ Create user
    """
    # TODO fix creating user with is_active=False
    return await service.user_s.create_user(schema)


# @admin_router.delete('/delete/{pk}', response_model=schemas.UserStatus, responses={404: {"model": HTTPNotFoundError}})
# async def delete_user(pk: int):
#     """ Delete user
#     """
#     deleted_count = await service.user_s.delete(id=pk)
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"Such user with id={pk} is not found")
#     return schemas.UserStatus(message="User has just been deleted")

@admin_router.put('/{pk}', response_model=schemas.UserInDB)
async def update_user(pk: int, schema: schemas.UserUpdate, user: models.User = Depends(get_superuser)):
    """ Update user
    """
    return await service.user_s.update(schema, id=pk)


@admin_router.delete('/{pk}', status_code=204)
async def delete_user(pk: int, user: models.User = Depends(get_superuser)):
    """ Delete user.
    """
    return await service.user_s.delete(id=pk)
