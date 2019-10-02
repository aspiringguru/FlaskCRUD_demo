# config.py

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    NB: these variable names are reserved. refer documentation
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    https://flask.palletsprojects.com/en/1.1.x/config/
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
