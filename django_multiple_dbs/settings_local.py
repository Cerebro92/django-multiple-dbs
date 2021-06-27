from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DATABASES = {
    'default': {},
    'students': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'colleges': {
        'NAME': 'colleges',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'mysql123'
    }
}
