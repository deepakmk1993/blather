## Starting from the Terminal

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate
    $ python manage.py runserver $IP:$PORT