from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField

class OutdoorAir(models.Model):
    id = models.ForeignKey('IndoorAir' ,on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now())
    characteristic = ArrayField(models.IntegerField())
    place = models.CharField(max_length=200)
    pm2_5 = models.IntegerField()
    temp = models.DecimalField()
    humidity = models.DecimalField()
