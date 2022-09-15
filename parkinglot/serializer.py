from rest_framework import serializers
from .models import Lot,Ticket
from caruser.serializer import UserSerializer
from carapp.serializer import CarSerializer

class LotSerializer(serializers.ModelSerializer):

    '''User serializer to display the user model:'''

    class Meta:
        model=Lot
        fields=['id','floor','slot','name','state',]


class TicketSerializer(serializers.ModelSerializer):

    '''Ticket serializer to display the  tickets...'''

    ticketowner=UserSerializer(required=True)
    vehicle=CarSerializer(required=True)
    lot=LotSerializer(required=True)
    class Meta:
        model=Ticket
        fields=['id','ticketstate','ticketowner','vehicle','lot',]



