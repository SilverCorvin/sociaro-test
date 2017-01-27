#!/bin/sh

sleep 10

cd video_previewer
su -m test -c "celery worker -A video_previewer.celeryconf -Q default -n deafult@%h"