import os
import dj_database_url
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: Mantener la clave secreta en secreto en producción
SECRET_KEY = 'django-insecure-52bqa!m^!rvqaz&2msc+yeqfe12i%(p$fh*+*=1y3#gysl(v-3'

# SEGURIDAD: DEBUG en False para producción (Azure)
# Puedes usar: DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
DEBUG = True

# Permitir el dominio de Azure y localhost
ALLOWED_HOSTS = ['help-desk-telecable.azurewebsites.net', '127.0.0.1', 'localhost', '*']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tickets',  # Tu aplicación principal
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Manejo de archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Base de Datos
# Configuración dinámica para Azure/Railway o SQLite local
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internacionalización
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# Archivos Estáticos (CSS, JS, Imágenes de diseño)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []

# Almacenamiento optimizado de archivos estáticos para producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Archivos Multimedia (Fotos de perfil, capturas de tickets)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de seguridad para formularios en la nube
CSRF_TRUSTED_ORIGINS = [
    'https://app-helpdesk-telecable-geeggsgfbuh5fwg7.centralus-01.azurewebsites.net',
    'https://*.azurewebsites.net',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Rutas de Autenticación
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'lista_tickets'
LOGOUT_REDIRECT_URL = 'login'

# --- CONFIGURACIÓN DE CORREO (GMAIL / OFFICE 365) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'area_ti@fibertheandes.com'
EMAIL_HOST_PASSWORD = 'cwth iggb egau vmdb'  # Contraseña de aplicación
DEFAULT_FROM_EMAIL = f'Help Desk Fiber The Andes <{EMAIL_HOST_USER}>'

# Configuración adicional para Azure (Evitar errores de sesión en HTTP)
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_REDIRECT = True