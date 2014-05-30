# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join
import ldap
from django_auth_ldap.config import LDAPSearch



BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdown_deux',
    'south',
    'excercise',
    'parsing',
    'easy_pdf',
    'django_cleanup',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'excercise.proxy.ProxyUserMiddleware',
)

ROOT_URLCONF = 'django_cn.urls'

WSGI_APPLICATION = 'django_cn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'users': {
        'NAME': 'moodle',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'host',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://example.com"
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=people,dc=cn,dc=ntua,dc=gr",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

STUDENT_ROLE_ID = 5
EXAMINER_ROLE_ID = 4 
TEACHER_ROLE_ID = 3

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    'django.core.context_processors.request',
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "excercise.context_processors.application",
)

USER_LOGIN_REDIRECT_URL = '/excercise/'
EXAMINER_LOGIN_REDIRECT_URL = '/excercise/examiner/'
GRAPPELLI_ADMIN_TITLE = 'CN admin'

try:
    from local_settings import *
except ImportError as e:
    pass
