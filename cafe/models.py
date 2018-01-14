from django.db import models

# Create your models here.
class CafeInfo(models.Model):
    name = models.CharField(max_length=50)
    address = model.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    power = models.IntegerField()
    americano = models.IntegerField()
    wifi = models.IntegerField()
    start_weekday = models.TimeField()
    start_sat = models.TimeField()
    start_sun = models.TimeField()
    end_weekday = models.TimeField()
    end_sat = models.TimeField()
    end_sun = models.TimeField()
