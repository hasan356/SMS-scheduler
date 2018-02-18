# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



#create your model here

class user(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)



