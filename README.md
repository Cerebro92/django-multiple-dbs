# Django Multiple DBs

This repository showcases a sample Django application connections with multiple databases.  SQLite and MySQL databases has been user for demo purpose which contains student and college tables respectively.


- Django template which allow multiple database connection.
- Manage Command to populate tables -- student & college.
- Pagination support added in List APIs.


## Installation
Project has been tested with Python 3.9


Clone the repository

```sh
git clone https://github.com/Cerebro92/django-multple-dbs.git
cd django-multple-dbs
```

Create Virtual environment and install packages

```sh
python3 -m venv venv
pip install -r requirements.txt
```

Change MySQL database credentials in `django_multiple_dbs/settings_local.py` file.
```sh
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
```

Create college DATABASE in MySQL DB.

```sh
CREATE DATABASE colleges
```

Run migrations for both DBs

```sh
python manage.py migrate --database=colleges
python manage.py migrate --database=students
```

Populate `college` and `student` tables

```sh
python manage.py populate_db college
python manage.py populate_db student --num_records=1000
```

Run Server
```sh
python manage.py runserver
```

Access endpoints in web browser
```sh
http://127.0.0.1:8000/college/list
http://127.0.0.1:8000/student/list
``` 