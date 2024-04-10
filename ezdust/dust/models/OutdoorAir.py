from django.db import models
import datetime

# Create your models here.
class OutdoorAir(models.Model):
    time = models.DateTimeField(default=datetime.datetime.now())
    place = models.CharField(max_length=200)
    pm2_5 = models.IntegerField()
    temp = models.DecimalField()
    humidity = models.DecimalField()
