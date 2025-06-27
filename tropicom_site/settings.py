import os
from pathlib import Path
import dj_database_url

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Sécurité
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-_t6%ciw3&g)h-8#617w(_u*%8w*1xmamd-075&rbi8k&3@xg%!'
)

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps personnelles
    'vitrine',
    'theme',
    'tailwind',

    # Utilitaires
    'django_browser_reload',
    'whitenoise.runserver_nostatic',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL principal
ROOT_URLCONF = 'tropicom_site.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'theme' / 'templates',  # pour le site public
            BASE_DIR / 'vitrine' / 'templates',  # pour l'admin personnalisé
        ],
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

WSGI_APPLICATION = 'tropicom_site.wsgi.application'

# Base de données
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
    )
}

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalisation
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
USE_L10N = True

LANGUAGES = [
    ('fr', 'Français'),
    ('en', 'English'),
    ('ar', 'العربية'),
    ('es', 'Español'),
]

LOCALE_PATHS = [BASE_DIR / 'locale']

# Fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'theme' / 'static',
    BASE_DIR / 'vitrine' / 'static',  # Ajout pour logo et admin.css personnalisés
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Tailwind CSS
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"  # Modifier selon ton OS si besoin

# Django Browser Reload
INTERNAL_IPS = ['127.0.0.1']

# Champs par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Envoi d'e-mails (SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'votre-email@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'votre-mot-de-passe')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
