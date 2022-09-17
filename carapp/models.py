from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ParkedCarManager(models.Manager):

    '''Get all parked cars...'''

    def get_queryset(self):
        return super().get_queryset().filter(state='PARKED')



class UnParkedCarManager(models.Manager):

    '''Get all unparked cars...'''

    def get_queryset(self):
        return super().get_queryset().filter(state='UNPARKED')


class Car(models.Model):

    '''Model for a car'''

    STATE = [('PARKED', 'Parked'), ('UNPARKED', 'Unparked')]

    carname=models.CharField(max_length=100)
    carowner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    carnumber=models.CharField(max_length=100)
    carcolor=models.CharField(max_length=20,default='NOCOLOR')
    registereddate=models.DateTimeField(auto_now=True,blank=False)
    state= models.CharField(max_length=20,choices=STATE,default='UNPARKED')
    objects=models.Manager()
    parkedcar=ParkedCarManager()
    unparkedcar=UnParkedCarManager()

    def __str__(self):
        return self.carname



