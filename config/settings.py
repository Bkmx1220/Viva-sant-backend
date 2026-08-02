"""
Paramètres Django du projet config.

Généré par 'django-admin startproject' avec Django 5.1.5.

Pour plus d’informations sur ce fichier, consultez
https://docs.djangoproject.com/en/5.1/topics/settings/

Pour la liste complète des paramètres et de leurs valeurs, consultez
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from decouple import config
from datetime import timedelta
# Construire les chemins à l’intérieur du projet ainsi : BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Paramètres rapides de développement - non adaptés à la production
# Voir https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# Clé secrète de l’application
SECRET_KEY = config("SECRET_KEY")

# Mode développement
DEBUG = config("DEBUG", cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])


# Définition des applications

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Paquets
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "corsheaders",

    # Applications
    "accounts",
    "users",
    "dashboard",
    "nutrition",
    "activity",
    "ai",
    "notifications",
    "common",
    "rest_framework_simplejwt.token_blacklist",
    "hydration",
    "goals",
    "analytics",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Base de données
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}


# Validation des mots de passe
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


# Internationalisation
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "Africa/Lome"

USE_I18N = True

USE_TZ = True

# Fichiers statiques (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Type de clé primaire par défaut
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        
    ),
     "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

SPECTACULAR_SETTINGS = {
    "TITLE": "VivaSanté API",
    "DESCRIPTION": "API REST officielle de VivaSanté",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Configuration du modèle utilisateur personnalisé
AUTH_USER_MODEL = "users.User"