from django.db import models
import datetime
# Create your models here.

class OutdoorAirAPI(models.Model):
    time = models.DateTimeField(default=datetime.datetime.now())
    place = models.CharField(max_length=200)
    pm2_5 = models.IntegerField()
    temp = models.FloatField()
    humidity = models.FloatField()

    class Meta:
        db_table = 'OutdoorAir'


class IndoorAirAPI(models.Model):
    outdoor = models.ForeignKey('OutdoorAirAPI', on_delete=models.CASCADE)
    place_type = (models.CharField(max_length=200))
    place = models.CharField(max_length=200)
    pm2_5 = models.IntegerField()
    temp = models.FloatField()
    humidity = models.FloatField()