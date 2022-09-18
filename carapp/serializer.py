from rest_framework import serializers
from caruser.serializer import UserSerializer
from carservice.serializer import CarServiceSerializer


class CarGroupSerializer(serializers.Serializer):

    '''Car serializer for displaying the cars registered by the user:'''

    id = serializers.IntegerField(read_only=True)
    groupname = serializers.CharField(required=True, allow_blank=False,max_length=100)
    services=CarServiceSerializer(required=True)

class CarSerializer(serializers.Serializer):

    '''Car serializer for displaying the cars registered by the user:'''

    id = serializers.IntegerField(read_only=True)
    carname = serializers.CharField(required=True, allow_blank=False,max_length=100)
    carnumber = serializers.CharField(required=True, allow_blank=False,max_length=100)
    carcolor =  serializers.CharField(required=True, allow_blank=False,max_length=100)
    carowner = UserSerializer(required=True)
    cargroup=CarGroupSerializer(required=True)
    registereddate=serializers.DateTimeField(required=True)




