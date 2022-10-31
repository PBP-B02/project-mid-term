from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Article_Cashflow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default= timezone.now)
    comment_anonymous = models.TextField()
