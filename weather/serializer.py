
from rest_framework import serializers

class Location(serializers.Serializer):
    location_id = serializers.AutoField(primary_key=True)
    location_name = serializers.CharField(max_length=100)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
class WeatherDataSerializer(serializers.Serializer):
    data_id = serializers.AutoField(primary_key=True)
    location = serializers.ForeignKey(Location, on_delete=serializers.CASCADE)
    datetime = serializers.DateTimeField()
    temperature = serializers.DecimalField(max_digits=10, decimal_places=2)
    air_quality = serializers.CharField(max_length=20)
    humidity = serializers.CharField(max_length=20)

   
