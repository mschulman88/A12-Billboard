# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class users(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=30)
    user_email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)