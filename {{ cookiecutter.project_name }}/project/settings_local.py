#DATABASES = { 
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': '{{ cookiecutter.project_name }}',
#    }   
#}
MONGODB = {
    'connection': {
        'host': 'localhost',
    },
    'dbname': '{{ cookiecutter.project_name }}',
}

SECRET_KEY = ''

ADMINS = ( 
)

INTERNAL_IPS = ()
DEBUG = True
ALLOWED_HOSTS = ['*']
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
