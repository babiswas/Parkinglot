from django.db import models

# Create your models here.

class Car(models.Model):

    '''Model for a car'''

    name=models.CharField(max_length=100)
    carid=models.CharField(max_length=100)
