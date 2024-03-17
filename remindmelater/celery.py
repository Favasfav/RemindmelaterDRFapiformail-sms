from __future__ import absolute_import, unicode_literals
import os 
from celery import Celery 
from django.conf import settings

# Set the default Django settings module for the 'celery' program. 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remindmelater.settings') 

app = Celery('remindmelater') 

# Using a string here means the worker doesn't 
# have to serialize the configuration object to 
# child processes. - namespace='CELERY' means all 
# celery-related configuration keys should 
# have a `CELERY_` prefix. 
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

# Set the serializer directly
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'json'
app.conf.accept_content = ['json']

app.config_from_object(settings, namespace='CELERY') 


app.conf.beat_schedule={
    
}                        

# Load task modules from all registered Django app configs. 
app.autodiscover_tasks() 

@app.task(bind=True)
def debug_task(self):
    print(f'request:{self.request!r}')
