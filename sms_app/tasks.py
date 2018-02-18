from celery.task import periodic_task
from celery.schedules import crontab
from .models import user
from .sent import sent_msg



#this function runs periodically every hour ber
@periodic_task(run_every=(crontab(minute = 0)), name="processing_sms")
def processing_sms():
    User = user.objects.all()
    for users in User:
        sent_msg(users)

