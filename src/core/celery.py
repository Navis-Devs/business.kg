import os
import django
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

app = Celery('core', broker='redis://redis:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Asia/Bishkek'

app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks(['apps.helpers'])
