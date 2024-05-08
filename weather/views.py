import constant
import requests
import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from weather.serializer import WeatherDataSerializer, status
from weather.models import WeatherData
from django.conf import settings


class WeatherAPIView(APIView):
    def get(self, request):
        api_key = settings.API_KEYS
        location = constant.HANOI_LOCATION
        url = settings.WEATHER_API_URL.format(city=location, api_key=api_key)

        response = requests.get(url, timeout=1)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            result = {
                "longitude": data["coord"]["lon"],
                "latitude": data["coord"]["lat"],
                "location": data.get("name"),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "windspeed": data["wind"]["speed"],
            }
            response = WeatherDataSerializer(result)
            return Response(response.data)
        elif status_code == 400:
            raise serializers.ValidationError("Error URL")
        else:
            return serializers.ValidationError("Error code")
