# -*- coding: utf-8 -*-
import logging
import os
import sys

from path import path

SITE_ID = 1

# Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = path(__file__).abspath().realpath().dirname().parent
PROJECT_NAME = PROJECT_DIR.basename()
SITE_DIR = PROJECT_DIR.parent
APPS_DIR = PROJECT_DIR / 'apps'
LIBS_DIR = PROJECT_DIR / 'libs'
sys.path.append(SITE_DIR)
sys.path.append(APPS_DIR)
sys.path.append(LIBS_DIR)

# Append directories to sys.path

# Root URLs module
ROOT_URLCONF = 'django-scatter.urls'

# WSGI application
WSGI_APPLICATION = 'django-scatter.wsgi.application'

##################################################################
# Language and timezone settings
##################################################################

# Specifies whether Django’s translation system should be enabled.
USE_I18N = True

# Specifies if localized formatting of data will be enabled by
# default or not.
USE_L10N = True

# Specifies if datetimes will be timezone-aware by default or not.
USE_TZ = False

# A string representing the time zone for this installation.
TIME_ZONE = 'Asia/Shanghai'

# A string representing the language code for this installation.
LANGUAGE_CODE = 'en'

##################################################################
# Authentication settings

AUTH_USER_MODEL = 'webuser.WebUser'
AUTHENTICATION_BACKENDS = ['webuser.backend.WebUserBackend']

# ######################### session #########################
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 259200
SESSION_COOKIE_NAME = "dsessionId"
# SESSION_COOKIE_DOMAIN = BROWSER_DOMAIN

##################################################################
# Middleware settings
##################################################################

# The default number of seconds to cache a page when the caching
# middleware or cache_page() decorator is used.
CACHE_MIDDLEWARE_SECONDS = 5

# The cache key prefix that the cache middleware should use.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_NAME + '_'

# A tuple of middleware classes to use.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

##################################################################
# Static settings
##################################################################

# The absolute path to the directory where collectstatic will
# collect static files for deployment.
STATIC_ROOT = ''

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# Additional locations the staticfiles app will traverse if the
# FileSystemFinder finder is enabled.
STATICFILES_DIRS = (
    PROJECT_DIR / 'static',
)

# The list of finder backends that know how to find static files
# in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

##################################################################
# Templates settings
##################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            PROJECT_DIR / 'templates',
        ],
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                # 'dj_csgo.context_processors.multi_site_static',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                # insert your TEMPLATE_LOADERS here
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

##################################################################
# Installed apps
##################################################################

EXTERNAL_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Other external apps
)

INTERNAL_APPS = (
    # Application specific apps
    'webuser',
    'django_tools',
)

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(funcName)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 按日期存储
        'file': {
            'level': 'ERROR',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': PROJECT_DIR / 'logs/django.log',
            'formatter': 'verbose'
        },
        'user_handler': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 1000,
            'backupCount': 10,
            'delay': True,
            'filename': PROJECT_DIR / 'logs/user.log',
            'formatter': 'verbose'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_tools.DynamicSite': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'user': {
            'handlers': ['user_handler'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# ######################## service #############################
