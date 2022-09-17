from django.db import models
from django.contrib.auth.models import User
from carservice.models import CarService
from django.db import transaction

# Create your models here.


class CarGroup(models.Model):

    '''Car group for associating car with a service.'''

    groupname=models.CharField(max_length=100)
    services=models.ForeignKey(CarService,on_delete=models.CASCADE)


    def __str__(self):
        return self.groupname

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
    cargroup=models.ForeignKey(CarGroup,on_delete=models.CASCADE,default=1)
    objects=models.Manager()
    parkedcar=ParkedCarManager()
    unparkedcar=UnParkedCarManager()

    def __str__(self):
        return self.carname









