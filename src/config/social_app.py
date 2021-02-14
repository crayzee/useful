from authlib.integrations.starlette_client import OAuth


social_oauth = OAuth()

social_oauth.register(
    name='github',
    client_id='99118809b9098fa3fa00',
    client_secret='a5899c5cb8ddc411a241880d0ebf362a3098cb8a',
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params = None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)
