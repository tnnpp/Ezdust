from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField

class Health(models.Model):
    time = models.DateTimeField(default=datetime.datetime.now())
    patient_number = models.IntegerField()
    place = models.CharField(max_length=200)
