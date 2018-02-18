from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amnesia.settings')

app = Celery('amnesia')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings', namespace='CELERY')

# With the line below Celery will automatically discover tasks from all of your installed apps,
# following the tasks.py convention:
app.autodiscover_tasks()


# Finally, the debug_task example is a task that dumps its own request information.

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))



