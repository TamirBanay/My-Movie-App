"""
Django settings for movies_app project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-20n-d2+d%wbjkn(z02+bor%64cila#ygv84$w0#osme@muvl40'
TMDB_API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MzM3NTJiZjE3MmJlMzNhNTdhY2UyNTAxYjI5MDkyYSIsInN1YiI6IjY1MDE5YWJjNmEyMjI3MDBhYmE5MWFlNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6EhZEXn1Bz9SFSO4_zALQKSY6DRvx_O7-tdzP1J_Ls0"



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
   
}

SIMPLE_JWT = {
     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
     'ROTATE_REFRESH_TOKENS': True,
     'BLACKLIST_AFTER_ROTATION': True
}



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members',
    'movies_app',
    'corsheaders',
    'rest_framework',




]
LOGIN_URL = 'login'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
    "http://localhost:8080",

]
CORS_ALLOW_ALL_ORIGINS = True

AUTH_USER_MODEL = 'members.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    

]

ROOT_URLCONF = 'movies_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'movies_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moviesSchema',
        'USER': 'root',
        'PASSWORD': "tamirsapir055",
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
