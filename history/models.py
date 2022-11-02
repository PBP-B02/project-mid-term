from django.db import models
from django.contrib.auth.models import User

class budgetHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    budget_type = models.TextField()
    month = models.IntegerField()
    totalAmount = models.IntegerField(null=True)
