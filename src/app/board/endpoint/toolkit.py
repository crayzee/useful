from typing import List

from fastapi import APIRouter
from .. import schemas, service


toolkit_router = APIRouter()


@toolkit_router.get('/', response_model=List[schemas.GetToolkit])
async def get_toolkit():
    return await service.toolkit_s.filter(parent_id__isnull=True)


@toolkit_router.post('/', response_model=schemas.GetToolkit)
async def create_toolkit(schema: schemas.CreateToolkit):
    return await service.toolkit_s.create(schema)
