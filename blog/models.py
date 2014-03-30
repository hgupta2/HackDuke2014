from django.db import models

# Create your models here.

class youtube(models.Model):

    title = models.CharField(max_length = 200)
    description = models.TextField()
    url = models.CharField(max_length = 200)
    view_count = models.IntegerField()
    thumbnail = models.CharField(max_length = 200)

class courses(models.Model):

    name = models.CharField(max_length = 200)
    description = models.TextField()
    url = models.CharField(max_length = 200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    level = models.IntegerField()
    site = models.CharField(max_length = 100)
