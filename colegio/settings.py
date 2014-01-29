"""
Django settings for colegio1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# encoding:utf-8
import sys
sys.path.append("/path/to/EasyBoard")
from EasyBoard.settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    ('Mauricio Aizaga', 'maizaga@daiech.com'),
    ('Soporte DEL', 'soporte@del.com.co'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$a-g%gkv7_31ql*^71$_)(*kmc5@=cln$#+ebs^kn*_s+ne6_b'

# SECURITY WARNING: don't run with debug turned on in production!
try:
    from .local_settings import DEBUG
except Exception:
    DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*.easyboard.co", "*.easyboard.com.co"]


# Application definition

APPS = [] # "apps desarrolladas para este cliente"

INSTALLED_APPS = INSTALLED_APPS + tuple(APPS)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'colegio.urls'

WSGI_APPLICATION = 'colegio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

try:
    from .local_settings import DATABASES
except Exception, e:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'colegio.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

try:
    from .local_settings import EMAIL_HOST_USER
except:
    EMAIL_HOST_USER = ""
try:
    from .local_settings import EMAIL_HOST_PASSWORD
except:
    EMAIL_HOST_PASSWORD = ""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.sep.join([BASE_DIR, 'public/media'])
MEDIA_URL = '/media/'

NEW_STATICFILES_DIRS = []  # ej: os.sep.join([BASE_DIR, 'apps/app4/static'])

STATICFILES_DIRS = STATICFILES_DIRS + tuple(NEW_STATICFILES_DIRS)
