from django.db import models
from django.utils import timezone


class OutdoorAir(models.Model):
    time = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=200)
    pm2_5 = models.IntegerField()
    temp = models.FloatField()
    humidity = models.FloatField()
