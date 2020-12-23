from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cars.models import Car


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Group model.
    """
    class Meta:
        model = Group
        fields = ['url', 'name']


class CarSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Car model.
    """
    class Meta:
        model = Car
        fields = ['url', 'manufacturer', 'model', 'engine_size', 'engine_cylinders']
