import os
from django.conf import settings
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DATABASES = settings.DATABASES

# we only need the engine name, as heroku takes care of the rest
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#     }
# }


# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'