from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Search(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article_name = models.CharField(max_length=155)

class Comment(models.Model):
    comment = models.CharField(max_length=155)
    
