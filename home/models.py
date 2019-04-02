from django.db import models

# Create your models here.

class home(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField(null=False,blank=False)
    message = models.TextField()

    def __str__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField(null=False,blank=False)
    message = models.TextField()

    def __str__(self):
        return self.name
