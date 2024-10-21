"""
Django settings for AltaPeli project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%1&th=x+-mqq3y-mw&8g2bcut^6h*po(9yz^b_2(cfo8te^%0t'



# URLS
#LOGIN_URL = '././apps//login/'  # URL de logueo
LOGIN_REDIRECT_URL = '/'  # URL a la que se redirige después de iniciar sesión
LOGOUT_REDIRECT_URL = 'login'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AltaPeli',
    'apps.Actores_Directores',
    'apps.Peliculas_Series',
    'apps.Sesiones',
    'storages'
]

    #'apps.Actores_Directores',
    #'apps.Listas',
    #'apps.Peliculas_Series',
    #'apps.Sesiones',
    

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AltaPeli.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
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

DEBUG = True

WSGI_APPLICATION = 'AltaPeli.wsgi.application'

AUTH_USER_MODEL = 'Sesiones.User'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')
STATICFILES_DIRS= (os.path.join(os.path.dirname(BASE_DIR), 'static'),)
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

AWS_ACCESS_KEY_ID= 'AKIAUGO4KT7F4OQ5M5W2'
AWS_SECRET_ACCESS_KEY= ''
AWS_STORAGE_BUCKET_NAME= 'altapelibucket '
AWS_S3_SIGNATURE_NAME= 's3v4'
AWS_S3_REGION_NAME= 'us-east-2'
AWS_S3_FILE_OVERWRITE= False
AWS_DEFAULT_ACL= None
AWS_S3_VERITY= True
DEFAULT_FILE_STORAGE= 'storages.backends.s3boto3.S3Boto3Storage'