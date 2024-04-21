from django.db import models
from django.utils import timezone


class IndoorAir(models.Model):
    outdoor = models.ForeignKey('OutdoorAir' ,on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=200)
    pm2_5 = models.IntegerField()
    temp = models.FloatField()
    humidity = models.FloatField()
