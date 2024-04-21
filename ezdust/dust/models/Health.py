from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Health(models.Model):
    time = models.DateTimeField(default=timezone.now)
    patient_number = models.IntegerField()
    place = models.CharField(max_length=200)
