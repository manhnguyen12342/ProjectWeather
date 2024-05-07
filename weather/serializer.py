from rest_framework import serializers,status


class LocationSerializer(serializers.Serializer):
    location_id = serializers.IntegerField()
    location_name = serializers.CharField(max_length=100)
   
    

class WeatherDataSerializer(serializers.Serializer):
    # data_id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    location = serializers.CharField()
    # datetime = serializers.DateTimeField()
    temperature = serializers.FloatField()
    # air_quality = serializers.CharField(max_length=20)
    humidity = serializers.IntegerField()
    windspeed = serializers.FloatField()
    # sunrise = serializers.DateField()
    # sunset =serializers.DateField()