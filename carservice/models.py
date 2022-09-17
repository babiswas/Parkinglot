from django.db import models

# Create your models here.


class CarService(models.Model):

    '''Car services for managing the cars...'''

    servicename=models.CharField(max_length=100,default='SERVICE')
    carwash=models.BooleanField(default=False)
    carmantainence=models.BooleanField(default=False)
    carparking=models.BooleanField(default=False)
    carsecurity=models.BooleanField(default=False)

    def __str__(self):
        return self.servicename
