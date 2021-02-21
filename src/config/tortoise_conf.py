from src.config.settings import DATABASE_URI

TORTOISE_ORM = {
    "connections": DATABASE_URI,
    "apps": {
        'models': {
            "models": [
                "src.app.user.models",
                "src.app.auth.models",
                "src.app.board.models",
                "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
