import os
from dotenv import load_dotenv
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('DATABASE_HOST'),
        'PORT': env.str('DATABASE_PORT', default = 5434),
        'NAME': env.str('DATABASE_NAME'),
        'USER': env.str('DATABASE_USER'),
        'PASSWORD': env.str('DATABASE_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', default = False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
