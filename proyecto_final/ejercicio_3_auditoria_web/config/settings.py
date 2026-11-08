from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'clave-solo-para-desarrollo-cambiar-en-produccion'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['sustentabilidad']
ROOT_URLCONF = 'config.urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [BASE_DIR / 'templates'], 'APP_DIRS': True, 'OPTIONS': {'context_processors': ['django.template.context_processors.request']}}]
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Mendoza'
USE_TZ = True
STATIC_URL = 'static/'
