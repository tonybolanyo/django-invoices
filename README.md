# django-invoices

[![Build Status](https://travis-ci.org/tonybolanyo/django-invoices.svg?branch=master)](https://travis-ci.org/tonybolanyo/django-invoices) [![Coverage Status](https://coveralls.io/repos/github/tonybolanyo/django-invoices/badge.svg?branch=master)](https://coveralls.io/github/tonybolanyo/django-invoices?branch=master)

## Installation

First of all you need to download last version from the github repository

```
$ git clone https://github.com/tonybolanyo/django-invoices.git
```

After download finished, as any django project, you must follow this simple steps:

```
$ cd django-invoices
$ virtualenv env
$ env/bin/activate
$ pip install -r requirements/base.txt
$ cd src
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

After this you can see the API on your localhost. You need to login with the superuser created previously to view,
create, edit or delete any object with the API. By default, only staff can use the API.

You can change the default permissions using the Django Rest Framework settings:

**django-invoices/settings/base.py**
```
...
# Set default permission for API.
# Only staff can access API

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
...
```

