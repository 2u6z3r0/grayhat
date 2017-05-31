import os
from django.conf import settings
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

#disqus setup
DISQUS_API_KEY = 'PJpRGLPMlp9nKc97zPtZAKJBPZT484KSTePTz6RRRGErGswul1RJryQ25Mijwimc'
DISQUS_WEBSITE_SHORTNAME = 'grayhat-heroku'

# DATABASES = settings.DATABASES

# we only need the engine name, as heroku takes care of the rest
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
 }


# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# static files config
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static', 'static_dirs'),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'report.grayhat@gmail.com'
EMAIL_HOST_PASSWORD = 'Maxy675689'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = 'report.grayhat@gamil.com'

ADMINS = [('Maxadmin', 'samrat.patil0202@gmail.com')]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'app': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}