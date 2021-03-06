"""
Django settings for platzigram project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Directorio donde esta corriendo el proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# es usado para el hash de las contrasenas y las sesiones de las BD
SECRET_KEY = "6-x-o+wy%rvz$l$!h@$jw6rk0te8=@k6s&nemz+nj6sx^qn%nh"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Que hosts estan permitidos interactuar con nuestro proyecto
ALLOWED_HOSTS = []


# Que aplicaciones estan ligadas a nuestro proyecto django

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local apps
    "posts",
    "users",
]


# similar a APPS lo veremos mas adelante

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "platzigram.middleware.ProfileCompletionMiddleware",
]

# definimos nuestro archivo principal de urls.
ROOT_URLCONF = "platzigram.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        # APP_DIRS: Busca dentro de cada app un folder de name templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Archivo de entrada que se crea por defecto cuando creamos el proyecto
WSGI_APPLICATION = "platzigram.wsgi.application"


# Configuracion de la base de datos.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Validacion de password si estamos utilizando la autenticacion de django
# podemos crear diferentes validadores
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

# traduccion
USE_I18N = True

# traduccion
USE_L10N = True

# libreria de time zone
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Define que cada vez que vaya a /static/ en lugar de resolver la ruta
# usando el archivo urls.py va buscar resolver el archivo estatico
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# ruta absoluta del MEDIA_ROOT
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# directorio que sera declarado como media
MEDIA_URL = "/media/"

# redirecciona aca si intenta acceder a un recurso protegido
LOGIN_URL = "login"
