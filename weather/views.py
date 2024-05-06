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
            ans={
                "location":data["name"],
                "temperature":data["main"]["temp"],
                "humidity":data["main"]["humidity"],
                
            }
            serializer = WeatherDataSerializer(data=ans)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        
        def post(self, request):
            
            serializer = WeatherDataSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class Atherods(APIView):
    def post(self, request):
        serializer = WeatherDataSerializer(data=request.data)
        if serializer.is_valid():
            temperature = serializer.validated_data['temperature']
            humidity = serializer.validated_data['humidity']
    
            if temperature > 20 or humidity > 0 :
                return Response({"message": "Cảnh báo: Điều kiện thời tiết nguy hiểm!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Điều kiện thời tiết bình thường"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
            
            
        
