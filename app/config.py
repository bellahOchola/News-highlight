class Config:
    '''
    General configuration parent class
    '''
    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?&country=us&{}&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'



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
