"""
Django settings for NewSite project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
COMING_SOON = True
if COMING_SOON:
    MAINTENANCE_MODE_TEMPLATE = "coming_soon.html"
else:
    MAINTENANCE_MODE_TEMPLATE = "503.html"





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'maintenance_mode',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    "debug_toolbar",
    "django_htmx",
    'imagekit',
    'storages',
    'django_summernote',


]

SITE_ID = 1

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware', #maitenence mode middleware must be at end
]

ROOT_URLCONF = 'NewSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.custom_context_processor.user_info',
                'main.custom_context_processor.post_info',
                'main.custom_context_processor.category_info',
                'main.custom_context_processor.tags_info',
                'main.custom_context_processor.general_settings',


            ],
        },
    },
]

WSGI_APPLICATION = 'NewSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

live_deploy = True

if live_deploy == True:

    ALLOWED_HOSTS = ['*', 'https://photographysite-production.up.railway.app']

    CSRF_TRUSTED_ORIGINS = ['https://photographysite-production.up.railway.app']

    DATABASES = {
        'default': {
            'NAME': env("DATABASE_NAME"),
            'ENGINE': 'django.db.backends.postgresql',
            'USER': env('DATABASE_USER'),
            'PASSWORD': env('DATABASE_PASSWORD'),
            'HOST': env("DATABASE_HOST"),
            'PORT': env("DATABASE_PORT"),
        }
    }


elif live_deploy == False:

    ALLOWED_HOSTS = ['127.0.0.1', ]

    DATABASES = {
        'default': {
            'NAME': env("DEV_DATABASE_NAME"),
            'ENGINE': 'django.db.backends.postgresql',
            'USER': env('DEV_DATABASE_USER'),
            'PASSWORD': env('DEV_DATABASE_PASSWORD'), }
    }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True











# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [

    "127.0.0.1",

]


AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'NewSite.storage_backends.CustomS3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATICFILES_FINDERS = (           'django.contrib.staticfiles.finders.FileSystemFinder',
                                  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


IMAGEKIT_DEFAULT_IMAGE_CACHE_BACKEND = 'imagekit.imagecache.NonValidatingImageCacheBackend'


SUMMERNOTE_CONFIG = {

    'attachment_filesize_limit': 30000000,

}

SUMMERNOTE_THEME = 'bs4'