from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    tanggal = models.DateTimeField(auto_now_add=True)
    konten = models.TextField()
    

