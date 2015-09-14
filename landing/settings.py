# coding=utf-8
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_tpd9(a+n4i20i$5j6$cw^%09q=i6_r1e-j8ur-e@uw91#g@hd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['elitkadom.ru', u'арт-лифт.рф']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'admin@elitkadom.ru'
EMAIL_HOST = 'smtp.fullspace.ru'
EMAIL_HOST_USER = 'admin@elitkadom.ru'
EMAIL_HOST_PASSWORD = 'alena2010'


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'imagekit',
    'widget_tweaks',
    'annoying',
    'core',
    'apps.slider',
    'apps.address',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'core.context.site_setup',
)

INTERNAL_IPS = '127.0.0.1'
ROOT_URLCONF = 'landing.urls'

WSGI_APPLICATION = 'landing.wsgi.application'

DEBUG_TOOLBAR_PATCH_SETTINGS = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.mysql',
#          'NAME': 'elitkadoru',
#          'USER': 'elitkadoru',
#          'PASSWORD': 'd9310cfa',
#          'HOST': 'localhost',
#          'PORT': '',
#      }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'Landing',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        # {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'label': u'Настройки', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group', 'core.setup')},
        {'label': u'Контакты', 'icon': 'icon-cog', 'models': ('core.contacts',)},
        {'label': u'Заявки', 'icon': 'icon-user', 'models': ('core.ticket',)},
        {'label': u'Районы', 'models': ('core.area',)},
        {'label': u'Слайдер', 'app': 'slider',},
        {'label': u'Адресная программа', 'app': 'address',},
    ),
}

SLIDER_SIZE = [525, 350]
ADDRESS_SIZE = [280, 280]
ADDRESS_ITEM_SIZE = [700, 700]
