from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
