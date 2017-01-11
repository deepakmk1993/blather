# Deploying Python and Django Apps on Heroku
ALLOWED_HOSTS = ['.herokuapp.com','127.0.0.1']

    ====================================================================================================================
    1) Run below command to sync models to database and create Django's default superuser and auth system and Run Django
    ====================================================================================================================
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver $IP:$PORT

    ====================
    2) Create Virtualenv
    ====================
    $ virtualenv venv
    $ source venv/bin/activate

    ===========
    3) Procfile
    ===========
    web: gunicorn gettingstarted.wsgi --log-file -

    =========================
    4) Database configuration
    =========================
    Install "psycopg" & "dj-database-url" with the following commands:
    $ sudo easy_install psycopg2
    $ sudo easy_install dj-database-url
    settings.py
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)

    =============
    5) WhiteNoise
    =============
    $ pip install whitenoise

    wsgi.py
        from django.core.wsgi import get_wsgi_application
        from whitenoise.django import DjangoWhiteNoise
        
        application = get_wsgi_application()
        application = DjangoWhiteNoise(application)

    =====================================
    6) Serving static files in production
    =====================================
    settings.py
        PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
        STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
        
        STATIC_URL = '/static/'
        
        # Extra places for collectstatic to find static files.
        STATICFILES_DIRS = (
            os.path.join(PROJECT_ROOT, 'static'),
        )
    mkdir static
    Run below command if folder is empty because if your folder is empty then git doesn't commit them
    touch static/.dir
    $ python manage.py collectstatic --noinput

    ===============
    7) Requirements
    ===============
    $ pip freeze > requirements.txt
        Django==1.9
        dj-database-url==0.4.2
        gunicorn==19.6.0
        psycopg2==2.6.2
        whitenoise==3.2.3