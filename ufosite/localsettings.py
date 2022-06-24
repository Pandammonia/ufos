SECRET_KEY = 'django-insecure-ty8$c8=rv6kipt$6(w((h(7&x$k!pycylkjw7zp3^e0=*uv00z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ufosite',
        'USER': 'postgres',
        'PASSWORD': 'Peacock',
        'HOST': '',
        'PORT': '',
    }
}