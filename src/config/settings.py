import os
from .local_config import *

PROJECT_NAME = "Useful"
SERVER_HOST = 'http://127.0.0.1:8000'

# Secret key
SECRET_KEY = b"laksd^8223kad_)8dkfjslkjUJKSN83_*Kk3ja@8ksdfj"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_V1_STR = "/api/v1" 

# Token 60 minutes * 24 hours * 7 days = 7 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

# CORS
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8080",
]

# Data Base via Docker 
# SQLALCHEMY_DATABASE_URI2 = (
#     f'postgresql://{os.environ.get("POSTGRES_USER")}:'
#     f'{os.environ.get("POSTGRES_PASSWORD")}@'
#     f'{os.environ.get("POSTGRES_HOST")}/'
#     f'{os.environ.get("POSTGRES_DB")}'
# )
# Data Base
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://postgres:oilgas@localhost/useful"
)


USERS_OPEN_REGISTRATION = True

EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = "src/email-templates/build"

# Email
# SMTP_TLS = os.environ.get("SMTP_TLS")
# SMTP_PORT = os.environ.get("SMTP_PORT")
# SMTP_HOST = os.environ.get("SMTP_HOST")
# SMTP_USER = os.environ.get("SMTP_USER")
# SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
# EMAILS_FROM_EMAIL = os.environ.get("EMAILS_FROM_EMAIL")

EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL
EMAIL_TEST_USER = "twopik@gmail"
