from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.WeatherDataDetail.as_view()),
    path('Location/',views.LocationDetail.as_view()),
]