from .base import *
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogdb',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'PORT': '5432',
        'HOST': 'localhost'
    }
}
