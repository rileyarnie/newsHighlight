import os



class Config:
    API_KEY=os.environ.get("NEWS_API_KEY")
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?language=en&country=us&apiKey={}'
    NEWS_ARTICLES_API_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SECRET_KEY = os.environ.get("SECRET_KEY")

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
