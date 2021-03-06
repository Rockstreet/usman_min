"""
Django settings for smallcms project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GRAPPELLI_ADMIN_TITLE = "Система управления"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qc)5rh6*$n60cdxd21m!^0hzaflw*o*k@e+91^957+g0t9lybo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '185.22.60.239', 'caimanfishing.ru', 'www.caimanfishing.ru']



EMAIL_HOST = 'smtp.yandex.ru'

EMAIL_HOST_USER = 'sendfromsite@caimanfishing.ru'

EMAIL_HOST_PASSWORD = '24sendfromsite24'



EMAIL_PORT = '465'

EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ACCOUNT_ACTIVATION_DAYS = 10
REGISTRATION_OPEN = 2







# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    # 'grappelli.dashboard',
    'nested_admin',
    'grappelli',
    # 'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'adminsortable2',
    'taggit',
    'bootstrap3',
    'mptt',
    'easycart',
    'phonenumber_field',
    'django_mptt_admin',
    'geoposition',
    'embed_video',
    'sorl.thumbnail',
    'page',
    'smallcms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'smallcms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'smallcms', 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'page.context_processors.context',
                'page.context_processors.sitting',

            ],
            'libraries': {  # Adding this section should work around the issue.
                #'cms_tags': 'smallcms.templatetags.cms_tags',  # to add new tags module,
            },
        },
    },
]

WSGI_APPLICATION = 'smallcms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        # 'CONN_MAX_AGE': 0,
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'smallcms',
        # 'PASSWORD': 1,
        # 'PORT': 5432,
        # 'USER': 'postgres'
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'newusman_db_work',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'RU-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': '500',
        'width': '100%',
        'extraPlugins': 'youtube'
    },
}



# GEO MARKERS
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCe3oNO59ag4XLM3Yog7X8L77-PotI3DCA'
GEOPOSITION_MAP_OPTIONS = {
    'zoom': 6,
    'center': {'lat': 55.01886864032478, 'lng': 50.76003453124997},
    # 'mapMaker': True,
    'cursor': 'move',
}
GEOPOSITION_MARKER_OPTIONS = {
    # 'draggable': True,
    # 'clickable': True,
    'cursor': 'move',
    'position': {'lat': 55.01886864032478, 'lng': 50.76003453124997},
}

MENU_TEMPLATES = (
    # Customize this
    # (1, 'vertical_menu.html'),
    # (2, 'horizontal_menu.html')
)



APPLICATION_LIST = (
    # Applications for list in the page editor
    ('news', 'Приложение новости'),
)

CACHE_TIMEOUT = 86400 * 360 # one year
MYMENU_CACHE_KEY = 'menus'
CAROUSEL_CACHE_KEY = 'carousel'

NEWS_PAGINATE_BY = 10

THUMBNAIL_DEBUG = True
THUMBNAIL_FORCE_OVERWRITE = True

EASYCART_CART_CLASS = 'cart.views.Cart'