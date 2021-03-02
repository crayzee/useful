from fastapi import APIRouter
from src.app.board.endpoint import blogCategory, toolkit, project, task


board_router = APIRouter()

board_router.include_router(blogCategory.category_router, prefix='/category')
board_router.include_router(toolkit.toolkit_router, prefix='/toolkit')
board_router.include_router(project.project_router, prefix='/project')
board_router.include_router(task.task_router, prefix='/task')
