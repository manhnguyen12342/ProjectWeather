from rest_framework.views import APIView
from rest_framework.response import Response
from weather.serializer import WeatherDataSerializer,status
from weather.models import WeatherData
import requests
from django.conf import settings
import const

class WeatherAPIView(APIView):
    def get(self, request):
            
        api_key = settings.API_KEYS
        location = const.Hanoi_Location
        url = settings.WEATHER_API_URL.format(city=location,api_key=api_key)
            
        response = requests.get(url)
        data =  response.json()
        ans = {
            "location":data["name"],
            "temperature":data["main"]["temp"],
            "humidity":data["main"]["humidity"],
            }
        serializer = WeatherDataSerializer(ans)
        return Response(serializer.data)


class Atherods(APIView):
    def post(self, request):
        serializer = WeatherDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        temperature = serializer.validated_data['temperature']
        humidity = serializer.validated_data['humidity']
        if temperature > 20 or humidity > 0 :
           warning_message = 'Threshold exceeded for weather parameters.'
        else:
            warning_message = None
        return Response({'warning': warning_message})
    
            
            
        
