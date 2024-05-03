from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import WeatherDataSerializer,status
from .models import WeatherData
import requests
from django.conf import settings
import const

class WeatherAPIView(APIView):
        def get(self, request):
            
            api_key = settings.API_KEYS
            location = const.Hanoi_Location
            url = settings.WEATHER_API_URL.format(city=location,api_key=api_key)
            
            response = requests.get(url)
            data =response.json()
            # serializer = WeatherDataSerializer(data)
            # # # serializer.is_valid(raise_exception=True)
            return Response(data)
        
        def post(self, request):
            
            serializer = WeatherDataSerializer(request)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
            
            
        
