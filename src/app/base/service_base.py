# structure of service_base.py (logic)
# https://www.youtube.com/watch?v=H0jHvuYsIZ0&t=6689s
# time: 1:29:50 - 1:46:00

from typing import TypeVar, Type, Optional
from pydantic import BaseModel
from tortoise import models


ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)


class BaseService:
    model: Type[ModelType]
    create_schema: CreateSchemaType
    update_schema: UpdateSchemaType
    get_schema = GetSchemaType

    # def __init__(self, model: Type[ModelType]):
    #     self.model = model

    async def create(self, schema, **kwargs) -> Optional[CreateSchemaType]:
        obj = await self.model.create(**schema.dict(exclude_unset=True), **kwargs)
        return await self.get_schema.from_tortoise_orm(obj)

    async def update(self, schema, **kwargs):
        obj = await self.model.filter(**kwargs).update(**schema.dict(exclude_unset=True))
        return obj #await self.get_schema.from_tortoise_orm(obj)

    async def get(self):
        pass

    async def delete(self, schema):
        pass