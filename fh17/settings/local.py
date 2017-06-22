#settings/local.py

from .base import *

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fh',
        'USER': 'zac',
        'PASSWORD': 'confidence',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# Mailtrap.io
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'ff5bf54286842f'
EMAIL_HOST_PASSWORD = '0fe4318692fdfa'
EMAIL_PORT = '2525'
