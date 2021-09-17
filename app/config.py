from os import environ, getenv
from logging import DEBUG as log_debug

class ConfigFactory(object):
    def factory():
        env = environ.get("APP_SETTINGS", "Dev")
        conf = {
            'Dev': DevelopmentConfig(),
            'Prod': ProductionConfig()
        }

        return conf.get(env)

class Config:

    API_VERSION = "1.0"

    MONGODB_SETTINGS = {
        'db': getenv('DB_NAME'),
        'host': getenv('BD_HOST'),
        'username': getenv('USER'),
        'password': getenv('PASSWORD'),
        #'AUTHENTICATION_SOURCE': getenv('AUTHENTICATION_SOURCE')
    }

    #variables for logging the application
    LOGGER_NAME = environ.get('LOGGER_NAME', "logger")
    LOGGING = {
        'version': 1,
        'formatters': {
            'default': {
                'format': "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
            },
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': f"{getenv('APP_PATH')}/{LOGGER_NAME}.log",
            },
        },
        'loggers': {
            LOGGER_NAME: {
                'handlers': ['file', ],
                'level': log_debug
            },
        },
    }

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
