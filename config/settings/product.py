from .settings import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','https://analiz.darken.gen.tr/','analiz.darken.gen.tr']


CSRF_TRUSTED_ORIGINS = ['https://analiz.darken.gen.tr/', 'https://analiz.darken.gen.tr',]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT')
    }
}

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

