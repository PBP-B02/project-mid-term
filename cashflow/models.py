from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    date = models.DateField()
    name = models.TextField()
    amount = models.IntegerField()
    income_type = models.TextField()

class Spending(models.Model):
    date = models.DateField()
    name = models.TextField()
    amount = models.IntegerField()
    spending_type = models.TextField()

