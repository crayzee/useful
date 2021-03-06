from tortoise import fields, models, Tortoise

from src.app.user.models import User


class Category(models.Model):
    """ Categories by project
    """
    name = fields.CharField(max_length=150)
    parent: fields.ForeignKeyNullableRelation["Category"] = fields.ForeignKeyField(
        "models.Category", related_name="children", null=True
    )
    children: fields.ReverseRelation["Category"]
    projects: fields.ReverseRelation["Project"]

    class PydanticMeta:
        exclude = ['projects', 'parent']
        allow_cycles = True
        max_recursion = 4


class Toolkit(models.Model):
    """ Toolkit by project
    """
    name = fields.CharField(max_length=150)
    parent = fields.ForeignKeyField("models.Toolkit", related_name="children", null=True)
    projects: fields.ReverseRelation['Project']

    class PydanticMeta:
        exclude = ['projects', 'parent']
        allow_cycles = True
        max_recursion = 4


class Project(models.Model):
    """ Model for project
    """
    name = fields.CharField(max_length=150)
    description = fields.TextField()
    create_date = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField('models.User', related_name="user_projects")
    category: fields.ForeignKeyRelation[Category] = fields.ForeignKeyField(
        'models.Category', related_name="projects"
    )
    toolkit: fields.ForeignKeyRelation[Toolkit] = fields.ForeignKeyField(
        'models.Toolkit', related_name="projects"
    )
    team: fields.ManyToManyRelation[User] = fields.ManyToManyField(
        'models.User', related_name="team_projects", through="team_project"
    )
# TODO, you should add through="team_projects" in 'team' field


class Repository(models.Model):
    repo_id = fields.IntField()
    created_at = fields.DatetimeField()
    updated_at = fields.DatetimeField()
    stars = fields.IntField()
    forks = fields.IntField()
    watch = fields.IntField()
    topics = fields.CharField(max_length=1000)
    languages = fields.CharField(max_length=1000)
    description = fields.CharField(max_length=1000)


class Task(models.Model):
    """ Model task by project
    """
    description = fields.TextField()
    create_date = fields.DatetimeField(auto_now_add=True)
    start_date = fields.DatetimeField(null=True)
    end_date = fields.DatetimeField(null=True)
    project = fields.ForeignKeyField('models.Project', related_name="tasks")
    worker = fields.ForeignKeyField('models.User', related_name="tasks", null=True)


class CommentTask(models.Model):
    """ Model comment by task
    """
    user = fields.ForeignKeyField('models.User', related_name="task_comments")
    task = fields.ForeignKeyField('models.Task', related_name="comments")
    message = fields.CharField(max_length=1000)
    create_date = fields.DatetimeField(auto_now_add=True)


Tortoise.init_models(["src.app.board.models"], "models")
