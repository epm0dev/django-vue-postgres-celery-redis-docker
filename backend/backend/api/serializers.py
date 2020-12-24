from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    """
    Serializer for the Car model.
    """
    class Meta:
        model = Car
        fields = ['url', 'manufacturer', 'model', 'engine_size', 'engine_cylinders']
