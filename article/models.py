from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    

