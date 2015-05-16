# flake8: noqa
from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

LOGGING['loggers']['a2r_app']['level'] = 'DEBUG'
