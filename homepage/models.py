from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
 


