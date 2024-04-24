from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import WeatherDataSerializer
from .models import WeatherData
import requests
import os
from dotenv import load_dotenv
from django.conf import settings

class WeatherAPIView(APIView):
    def get(self, request):
        load_dotenv()
        api_key = settings.API_KEYS.format( )
        city = 'Hanoi'
        url = settings.WEATHER_API_URL.format(city=city, api_key=api_key)
        
        response = requests.get(url)
        data = response.json()
        
        temperature = data['main']['temp']
        humidity = data['main']['humidity'] 
        
        weather_data = {
            'city' : city,
            'temperature': temperature,
            'humidity': humidity,
        }
        serializer = WeatherDataSerializer(data=weather_data)
        serializer.is_valid(raise_exception=True)
        
        return Response(weather_data)
    
    def get_warning(self, request):
        weather_data = WeatherData.objects.all()
        if weather_data['temperature'] > 30  :
            return Response({'message': 'Temperature high'})
        elif weather_data['humidty'] >80:
            return Response({'message': 'Wet'})
        elif weather_data['temperature']<29:
            return Response({'message': 'Temperature high'})
        elif weather_data['humidty']<80 :
            return Response({'message': 'Dry'})
        else:
          return Response(weather_data)
 