from django.shortcuts import render
from rest_framework import generics
from .models import WeatherData,Location
from .serializer import WeatherDataSerializer,LocationSerrializer

class WeatherDataDetail(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
class LocationDetail(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerrializer
def check_thresholds(request):
    latest_weather_data = WeatherData.objects.latest('recorded_at')
    alerts = {}

    if latest_weather_data.temperature > 50:
        alerts['temperature'] = 'weather bad'
    else:
        alerts['temperature'] = 'Weather good'

    
    if latest_weather_data.humidity > 86 :
        alerts['humidity'] = 'humid weather!'
    else:
        alerts['humidity'] = 'good weather!'
    
    if latest_weather_data.air_quality <50 :
        alerts['air_quality'] = 'good air!'
    elif 51<latest_weather_data.air_quality <150:
        alerts['air_quality'] = 'average air!'
    else :
        alerts['air_quality'] ='bad air'
    
    return render({'alerts': alerts})