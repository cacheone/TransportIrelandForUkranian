import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    COUNTRY = 'Ireland'

    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'default_formatter': {
                'format': '[%(levelname)s:%(asctime)s] %(message)s'
            },
        },

        'handlers': {
            'stream_handler': {
                'class': 'logging.StreamHandler',
                'formatter': 'default_formatter',
            },
        },

        'loggers': {
            'my_logger': {
                'handlers': ['stream_handler'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }
