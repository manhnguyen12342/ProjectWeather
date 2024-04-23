from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import WeatherDataSerializer
import requests
import os
from dotenv import load_dotenv
from django.conf import settings

class WeatherAPIView(APIView):
    def get(self, request):
        api_key = settings.API_KEYS.format( )
        city = 'Hanoi'
        url = settings.WEATHER_API_URL.format(city=city, api_key=api_key)
        
        response = requests.get(url)
        data = response.json()
        
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        # air_quality = 'Not Available'  
        
        weather_data = {
             'city' : city,
            'temperature': temperature,
            'humidity': humidity,
            # 'air_quality': str(air_quality),  # Convert to string or another suitable format
        }
        serializer = WeatherDataSerializer(data=weather_data)
        serializer.is_valid(raise_exception=True)
        
        return Response(weather_data)
