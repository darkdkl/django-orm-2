import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('BASE_HOST'),
        'PORT': os.getenv('BASE_PORT'),
        'NAME': os.getenv('BASE_NAME'),
        'USER': os.getenv('BASE_USER'),
        'PASSWORD':os.getenv('BASE_USER_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True if os.getenv('DJANGO_DEBUG').lower() =='true' else False


ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

# USE_L10N = True
USE_L10N = False

TIME_ZONE = 'Europe/Moscow'

USE_TZ = False
LANGUAGE_CODE = 'ru-ru'
