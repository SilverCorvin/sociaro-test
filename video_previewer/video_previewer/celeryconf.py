import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video_previewer.settings')

app = Celery('video_previewer')

CELERY_TIMEZONE = 'Europe/Moscow'

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
