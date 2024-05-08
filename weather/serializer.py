from rest_framework import serializers

   
class WeatherDataSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    location = serializers.CharField()
    temperature = serializers.FloatField()
    humidity = serializers.IntegerField()
    windspeed = serializers.FloatField()