from datetime import datetime
from typing import List
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from . import models


CreateCategory = pydantic_model_creator(models.Category, exclude_readonly=True)
GetCategory = pydantic_model_creator(models.Category)


CreateToolkit = pydantic_model_creator(models.Toolkit, exclude_readonly=True)
GetToolkit = pydantic_model_creator(models.Toolkit, name='get_toolkit')


class Project(PydanticModel):
    name: str
    description: str
    create_date: datetime


class GetCategoryProject(PydanticModel):
    id: int
    name: str
    projects: List[Project]

    class Config:
        orm_mode = True




class CreateProject(PydanticModel):
    name: str
    description: str
    category_id: int
    toolkit_id: int
    user_id: int


class Category(PydanticModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class GetProject(PydanticModel):
    name: str
    description: str
    create_date: datetime
    # category: Category
    # toolkit: GetToolkit
    # team: List[UserPublic]

    # class Config:
    #     orm_mode = True


class CreateTask(PydanticModel):
    description: str
    start_date: datetime
    end_date: datetime
    project_id: int
    worker_id: int = None

    class Config:
        schema_extra = {
            "example": {
                "description": "string",
                "start_date": "2020-10-18 15:00:00",
                "end_date": "2020-10-19 15:00:00",
                "project_id": 0,
                "worker_id": 0
            }
        }


GetTask = pydantic_model_creator(models.Task, name='get_task')


class CreateCommentTask(PydanticModel):
    user_id: int
    task_id: int
    message: str


GetCommentTask = pydantic_model_creator(models.CommentTask, name='get_comment_task')
