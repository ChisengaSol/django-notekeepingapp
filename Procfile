release: python manage.py migrate
web: gunicorn keep_project.wsgi:application --log-file=-