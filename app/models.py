# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, default=0)
    
class FildsLocation(models.Model):
    field_name = models.CharField(max_length=200, default='')