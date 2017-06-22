#settings/local.py

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fh17',
        'USER': 'zac',
        'PASSWORD': 'confidence',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
