import environ
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',
    'https://business.navisdevs.ru'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # additional
    'channels',
    # 'daphne',
    'mptt',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'sorl.thumbnail',
    'colorfield',
    'versatileimagefield',
    'leaflet',
    'django_admin_geomap',
    'admin_extra_buttons',
    'parler',
    'debug_toolbar',
    'django_filters',
    'cachalot',

    # apps
    'apps.accounts',
    'apps.cars',
    'apps.cars_posts',
    'apps.house',
    'apps.main',
    'apps.tariffs',
    'apps.transactions',
    'apps.chat',
    'apps.helpers.api',
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    'DEFAULT_PAGINATION_CLASS': 'apps.helpers.paginations.StandardPaginationSet',
    'PAGE_SIZE': 50,

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.LocaleHeaderMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'apps.chat.middleware.TokenAuthMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

ASGI_APPLICATION = 'core.asgi.application'

DATABASES = {
    'default': env.db(),
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'business', 
#         'USER': 'navisdevs',
#         'PASSWORD': 'adminadmin',
#         'HOST': 'db',
#         'PORT': '5432',
#     }
# }

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

AUTH_USER_MODEL = "accounts.User"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Swagger

SPECTACULAR_SETTINGS = {
    'TITLE': 'Business KG',
    'DESCRIPTION': 'Api for Business KG',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# URL Settings

SITE_URL = env('SITE_URL', default='https://business.navisdevs.ru')

STATIC_URL = f'{SITE_URL}/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Variables

CELERY_BROKER_URL = 'redis://redis:6379/0'

EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

WATERMARK_PATH = 'media/watermark_logo/logo-1.png'

GMAIL_TEMPLATE_ADD = 'apps/helpers/send_mail_house.html'

GDAL_LIBRARY_PATH = env('GDAL_LIBRARY_PATH', default='/usr/lib/libgdal.so')


LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('kg', _('Kyrgyz')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'en',},
        {'code': 'ru',},
        {'code': 'kg',},
    ),
    'default': {
        'fallback': 'ru',
        'hide_untranslated': False,
    }
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "business.navisdevs.ru",
    # "172.19.0.5",
    # "0.0.0.0"
    # ...
]

def show_toolbar(request):
        return request.user.is_superuser

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}