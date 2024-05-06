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


class Weather_Altherods_Viewgi(APIView):
    def post(self, request):
        serializer = WeatherDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        temperature = request.data.get('temperature')
        humidity = request.data.get('humidity')
        if temperature > 30:
                warning = "High temperature warning!"
        elif humidity > 80:
                warning = "High humidity warning!"
        else:
                warning = None
        return Response({"status": "Weather data recorded.", "warning": warning}, status=status.HTTP_201_CREATED)
    
            
            
        
