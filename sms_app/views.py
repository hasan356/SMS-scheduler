# -*- coding: utf-8 -*-
from twilio.rest import TwilioRestClient
from django.shortcuts import render
from twilio.rest.lookups import TwilioLookupsClient
from twilio.rest.exceptions import TwilioRestException
from .models import user
from django.utils.timezone import utc
from datetime import datetime
from credentials import auth_token,account_sid

#this function check whether this is a valid number or not
def check_validity(number):
    try:
        client = TwilioLookupsClient(account_sid, auth_token)
        response = client.phone_numbers.get(number)
        return True
    except TwilioRestException as e:
        return False

def home(request):

    if request.method == 'POST':

        name = request.POST['name']
        number = request.POST['number']

        if not check_validity(number):
            return render(request , 'home_page.html' , {'error_message' : 'invalid_number'})

        try:
            User = user.objects.get(name=name, phone_number=number)
            return render(request, 'home_page.html',  {'error_message': 'This number already exists'} )
        except:

            try:
                client = TwilioRestClient(account_sid, auth_token)
                message = client.messages.create(body="Thank you for suscribing with this app", to=number, from_="+12092922212")
                User = user.objects.create(name=name, phone_number=number)
                return render(request , 'sms_sent.html')

            except TwilioRestException as e:
                return render(request, 'home_page.html', {'error_message': ' This Number is not verified'})








    return render(request, 'home_page.html')


# Create your views here.