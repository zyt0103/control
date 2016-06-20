"""
Django settings for control project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from kombu import Exchange
from kombu import Queue

from .config import setup_config
config = setup_config()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y4^5cd+@(9l6gzzjz#4n+-_inl=6r!1(4jaizm*$tqj*wa(+q7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    # 'django_crontab',
    'rest_framework',
)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
}

# CRONJOBS = [
#     ('/1* * * * *', "control.apps.modu.helper.signal_info_save"),
# ]
CONTROL_APPS = (
    'control.control',
    'control.apps.modu',
    'control.apps.demod',
)
INSTALLED_APPS += CONTROL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'control.control.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'control/control/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'control.control.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql' if config.get("database", "db_engine") == "mysql" else 'django.db.backends.sqlite3',
    'NAME': config.get("database", "db_name"),
    'USER': config.get("database", "db_user"),
    'PASSWORD': config.get("database", "db_password"),
    'HOST': config.get("database", "db_host"),
    'PORT': config.get("database", "db_port"),
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True

###############Redis Settings#######################
REDIS_HOST = config.get("redis", "host")
REDIS_PORT = config.get("redis", "port")
REDIS_PASSWORD = config.get("redis", "password")

REDIS_DB_CELERY = config.get("redis", "db_celery")
REDIS_DB_CELERY_BACKEND = config.get("redis", "db_celery_backend")

##############Celery Settings#######################
BROKER_URL = 'redis://:%s@%s:%s/%s' % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_DB_CELERY)
CELERY_SEND_EVENTS = config.getboolean("celery", "event")
CELERY_RESULT_BACKEND = 'redis://:%s@%s:%s/%s' % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_DB_CELERY_BACKEND)
if not config.getboolean("celery", "result"):
    del CELERY_RESULT_BACKEND
CELERY_TASK_SERIALIZER = "json"

# Result serialization format. Default is pickle.
CELERY_RESULT_SERIALIZER = "json"

# A white list of content-types/serializers to allow.
# If a message is received that is not in this list then the
# message will be discarded with an error.
CELERY_ACCEPT_CONTENT = ["json"]

# Configure Celery to use a custom time zones. The timezone value
# can be any time zones supported by the pytz library.
CELERY_TIMEZONE = config.get("celery", "timezone")

# If enabled dates and times in messages will be converted to use the UTC timezone.
CELERY_ENABLE_UTC = config.getboolean("celery", "enable_utc")

CELERY_DEFAULT_QUEUE = 'control'

CELERY_QUEUES = (
    Queue('control', Exchange('control'), routing_key='control'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/statics/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "statics"),
)

STATIC_ROOT = config.get("statics", "static_root")

########################NAMED_RULE##################
DISTRI_PREFIX = "distri"
PARTABLE_PREFIX = "partable"
TIMETABLE_PREFIX = "timetable"
AISDATA_PREFIX = "aisdata"
SIGNAL_PREFIX = "signal"
DEMOD_TYPE_PREFIX = "demodtype"
NAME_ID_LENGTH = 8

###################IF RUN MATLAB SETTINGS#############
IF_RUN_MATLAB = config.get("matlab", "runMatlab")

##################SAVE SIGNAL INFO PERIED ############
SAVE_PERIED = 1

##################DATABASE INFO ######################
DATABASE_USER = config.get("database", "db_user")
DATABASE_PWD = config.get("database", "db_password")