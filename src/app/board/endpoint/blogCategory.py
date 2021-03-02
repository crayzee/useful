from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError

from .. import schemas, service, models


category_router = APIRouter()


@category_router.post('/', response_model=schemas.GetCategory)
async def create_category(schema: schemas.CreateCategory):
    return await service.category_s.create(schema)


@category_router.get('/', response_model=List[schemas.GetCategory])
async def get_category():
    return await service.category_s.all()


@category_router.get('/{pk}', response_model=schemas.GetCategoryProject)
async def get_single_category(pk: int):
    query = await models.Category.get(id=1).prefetch_related('projects')
    # q = await query.fetch_related('projects')
    print(f'query = {query}')
    # print(f'q = {q}')
    s = schemas.GetCategoryProject.from_orm(query)
    print(s)
    return s # await models.Category.get(id=pk)#.select_related('projects')


@category_router.get('/all', response_model=schemas.GetCategories)
async def get_categories():
    categories = await service.category_s.get_all()
    return {
        "categories": categories
    }


@category_router.delete(
    '/delete/{category_id}', response_model=schemas.CategoryStatus, responses={404: {"model": HTTPNotFoundError}}
)
async def delete_category(category_id: int):
    """ Delete category
    """
    deleted_count = await service.category_s.delete(id=category_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Category with id={category_id} not found")
    return schemas.CategoryStatus(message=f"Deleted category {category_id}")
