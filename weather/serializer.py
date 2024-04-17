from rest_framework import serializers
from .models import WeatherData,Location

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
class LocationSerrializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'