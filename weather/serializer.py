
from rest_framework import serializers

class Location:
    def __init__(self, location_id, location_name, latitude, longitude):
        self.location_id = location_id
        self.location_name = location_name
        self.latitude = latitude
        self.longitude = longitude

class WeatherData:
    def __init__(self, data_id, location, datetime, temperature, air_quality, humidity):
        self.data_id = data_id
        self.location = location
        self.datetime = datetime
        self.temperature = temperature
        self.air_quality = air_quality
        self.humidity = humidity

class LocationSerializer(serializers.Serializer):
    location_id = serializers.IntegerField()
    location_name = serializers.CharField(max_length=100)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)

class WeatherDataSerializer(serializers.Serializer):
    data_id = serializers.IntegerField()
    location = serializers.SerializerMethodField()
    datetime = serializers.DateTimeField()
    temperature = serializers.DecimalField(max_digits=10, decimal_places=2)
    air_quality = serializers.CharField(max_length=20)
    humidity = serializers.CharField(max_length=20)

    def get_location(self, obj):
        return {
            'location_id': obj.location.location_id,
            'location_name': obj.location.location_name,
            'latitude': obj.location.latitude,
            'longitude': obj.location.longitude
        }
