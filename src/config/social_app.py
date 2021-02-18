from authlib.integrations.starlette_client import OAuth
from httpx import Timeout

social_oauth = OAuth()

redirect_uri = 'http://localhost:8000/api/v1/auth/github_login'

social_oauth.register(
    name='github',
    client_id='99118809b9098fa3fa00',
    client_secret='a5899c5cb8ddc411a241880d0ebf362a3098cb8a',
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,

    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email', 'timeout': Timeout(timeout=13)},
)
