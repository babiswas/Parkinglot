from rest_framework import serializers
from caruser.serializer import UserSerializer


class CarServiceSerializer(serializers.Serializer):

    '''Car serializer for displaying the cars registered by the user:'''

    id = serializers.IntegerField(read_only=True)
    servicename = serializers.CharField(required=True)
    carwash = serializers.BooleanField(required=True)
    carmantainence = serializers.BooleanField(required=True)
    carparking = serializers.BooleanField(required=True)
    carsecurity = serializers.BooleanField(required=True)
