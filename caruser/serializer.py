from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    '''User serializer to display the user model:'''

    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

