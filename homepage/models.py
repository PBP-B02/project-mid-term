from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Article_Cashflow(models.Model):
    date = models.DateTimeField(default= timezone.now)
    comment_anonymous = models.TextField()
