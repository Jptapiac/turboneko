"""
Settings de Django para el proyecto turboneko.
Listo para desarrollo local y pruebas en LAN (0.0.0.0:8000).
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-secret-key-cambia-en-produccion'
DEBUG = True  # en producción => False
ALLOWED_HOSTS = ["*"]  # en producción coloca tu dominio/IP específica

# Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
    'core',  # nuestra app
    'animatronics.apps.AnimatronicsConfig',
    'contract.apps.ContractConfig',  # app de contacto
]

# Crispy Forms Config
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'turboneko.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Usaremos carpeta "templates" a nivel del proyecto
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,  # permite templates dentro de las apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.global_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'turboneko.wsgi.application'

# Base de datos por defecto (sqlite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators (puedes dejarlos así en desarrollo)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos (CSS/JS/Imgs)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']   # carpeta "static" del proyecto
STATIC_ROOT = BASE_DIR / 'staticfiles'     # para collecstatic en producción

# Archivos media (si más adelante los usaras)
MEDIA_URL = '/media/'
# Si BASE_DIR es Path (Pathlib)
MEDIA_ROOT = BASE_DIR / 'media'
# Si BASE_DIR es string, usa:
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
