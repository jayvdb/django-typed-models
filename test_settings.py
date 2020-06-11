import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = ('typedmodels', 'django.contrib.contenttypes')
MIDDLEWARE_CLASSES = ()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
SECRET_KEY = 'abc123'
