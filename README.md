# Django Logger
Log exceptions, errors and user activity for Django

## Installation
Install with pip:
> pip install dj-logger

## Quick start
1. Add "django_logger" to your INSTALLED_APPS setting like this::

> INSTALLED_APPS = [ ... 'django_logger', ]
2. Add 'django_logger.middleware.RequestLoggingMiddleware' to your MIDDLEWARE setting like this::
   
> MIDDLEWARE = [
>
>    ...,
>
>    'django_logger.middleware.RequestLoggingMiddleware',
>
>    ]
3. Run python manage.py migrate to create the django_logger models.
4. Visit http://127.0.0.1:8000/admin/ to see logs.

## License
Django Logger is released under the terms of the **BSD 3-Clause**. Full details in ``LICENSE`` file.
