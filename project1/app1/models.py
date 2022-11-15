from django.db import models

# Create your models here.
from unicodedata import name

# Create your models here.
class Que(models.Model):
    firstName=models.CharField(max_length=100, blank=True)
    lastName=models.CharField(max_length=100, blank=True)
    emailId=models.CharField(max_length=254, blank=True)
    password=models.CharField(max_length=50, blank=True)
    confirmPassword=models.CharField(max_length=50, blank=True)
   
    def __str__(self):
        return self.firstName