from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import WeatherDataSerializer,status
from .models import WeatherData
import requests
from django.conf import settings
import const

class WeatherAPIView(APIView):
    def get(self, request):
        
        city = const.Hanoi_Location
        api_key = settings.API_KEYS.format(city=city)
        url = settings.WEATHER_API_URL.format(city=city,api_key=api_key)
        
        response = requests.get(url)
        data = response.json()
        serializer = WeatherDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
    
        return Response(serializer.data)
        
def post(self, request):
        serializer = WeatherDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
