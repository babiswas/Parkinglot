from django.db import models
from django.contrib.auth.models import User
from carapp.models import Car

# Create your models here.


class Lot(models.Model):

    '''Model for parking lot'''

    STATE=[('AVAILABLE','Available'),('OCCUPIED','Occupied'),('MANTAINENCE','Mantainence')]

    floor=models.IntegerField()
    slot=models.IntegerField()
    name=models.CharField(max_length=50)
    state=models.CharField(max_length=20,choices=STATE,default='AVAILABLE')

    def __init__(self):
        return self.name

class Ticket(models.Model):

    '''Model for ticket'''

    STATE = [('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')]

    ticketowner=models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Car,on_delete=models.CASCADE)
    lot=models.ForeignKey(Lot,on_delete=models.CASCADE)
    ticketstate=models.CharField(max_length=20,choices=STATE,default='ACTIVE')


    def __init__(self):
        return self.ticketstate


