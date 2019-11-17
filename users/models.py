from django.db import models
from home.models import home
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField(null=False,blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name