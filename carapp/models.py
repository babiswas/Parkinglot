from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):

    '''Model for a car'''

    carname=models.CharField(max_length=100)
    carowner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    carnumber=models.CharField(max_length=100)
    carcolor=models.CharField(max_length=20,default='NOCOLOR')
    registereddate=models.DateTimeField(auto_now=True,blank=False)


    def __init__(self):
        return self.carname
