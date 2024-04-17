from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class WeatherData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    air_quality = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)

# class AlertThresholds(models.Model):
#     parameter_id = models.IntegerField() 
#     threshold_value = models.DecimalField(max_digits=10, decimal_places=2)
