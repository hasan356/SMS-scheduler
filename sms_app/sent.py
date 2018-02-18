from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException
from credentials import account_sid,auth_token,starttime,endtime
from datetime import datetime
import pytz
import phonenumbers
from phonenumbers import timezone
from django.utils.timezone import utc


#Function actually sent the messages using TwilioRestClient
def sent_msg(users):

    if working_hours(users.phone_number):
        client = TwilioRestClient(account_sid , auth_token)
        f = open('log.txt' , 'a')
        phone_number = phonenumbers.parse(users.phone_number, None)
        curr_timezone = timezone.time_zones_for_number(phone_number)[0]
        now = datetime.now(pytz.timezone(curr_timezone))
        time = datetime.utcnow().replace(tzinfo=utc)
        diff_time = time - users.created_at
        no_of_attempts = 0
        while no_of_attempts < 5:
            try:
                message = "Hi!! your name is " + users.name
                client.messages.create(body=message  , to=users.phone_number , from_="+12092922212")

                f.write("%s Message sent successfully to %s running for %s\n" % (now, users. phone_number, diff_time ))
            except TwilioRestException as e:

                f.write("Error : %s message not sent due to technical issue to  %s running for %s\n" % (now, users.phone_number , diff_time))
                no_of_attempts = no_of_attempts + 1
                f.close()

#if the time is within the working hours then it return true else return false
def working_hours(number):
    phone_number = phonenumbers.parse(number, None)
    curr_timezone = timezone.time_zones_for_number(phone_number)[0]
    now = datetime.now(pytz.timezone(curr_timezone))
    if starttime<= now.hour <= endtime:
        return True
    else:
        return False

