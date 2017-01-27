#!/bin/sh


sleep 10

cd video_previewer

su -m test -c "python manage.py makemigrations video_previewer"
su -m test -c "python manage.py migrate"
su -m test -c "python manage.py runserver 0.0.0.0:8000"