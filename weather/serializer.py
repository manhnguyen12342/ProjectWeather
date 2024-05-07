from rest_framework import serializers,status


class LocationSerializer(serializers.Serializer):
    location_id = serializers.IntegerField()
    location_name = serializers.CharField(max_length=100)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    

class WeatherDataSerializer(serializers.Serializer):
    # data_id = serializers.IntegerField()
    location = serializers.CharField()
    # datetime = serializers.DateTimeField()
    temperature = serializers.FloatField()
    # air_quality = serializers.CharField(max_length=20)
    humidity = serializers.IntegerField()
