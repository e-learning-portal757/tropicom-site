from pathlib import Path
import os
import dj_database_url  # Assure-toi que ce package est dans requirements.txt

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY sécurisé via variable d'environnement
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-_t6%ciw3&g)h-8#617w(_u*%8w*1xmamd-075&rbi8k&3@xg%!'
)

# DEBUG est False en production, activé par variable d'environnement
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Autorisation des hôtes pour la prod (Render) et le dev local
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

# Applications installées
INSTALLED_APPS = [
    # Apps Django de base
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tes apps perso
    'vitrine',
    
    # Tailwind CSS
    'tailwind',
    'theme',
    
    # Auto reload du navigateur en dev
    'django_browser_reload',
    
    # WhiteNoise pour servir les fichiers statiques en prod
    'whitenoise.runserver_nostatic',
]

# Middleware avec WhiteNoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Important pour Render
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tropicom_site.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'theme' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Important pour admin, auth, etc.
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tropicom_site.wsgi.application'

# Configuration base de données via dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',  # fallback sqlite en local
        conn_max_age=600,
    )
}

# Validators mot de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Langue et fuseau horaire
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuration des fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'theme' / 'static',  # dossier static pendant le dev
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # dossier où collectstatic place les fichiers en prod

# WhiteNoise pour servir fichiers statiques en prod, avec compression & caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Django Tailwind
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"  # ajuste selon ton environnement

# Clé par défaut pour les nouveaux modèles
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
