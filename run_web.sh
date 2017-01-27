#!/bin/sh


sleep 10

cd video_previewer

su -m test -c "python manage.py migrate manager zero"
su -m test -c "python manage.py makemigrations"
su -m test -c "python manage.py migrate"
su -m test -c "python manage.py loaddata --app manager video_category.xml"
su -m test -c "python manage.py collectstatic --noinput"
su -m test -c "gunicorn video_previewer.wsgi -b 0.0.0.0:8000"