# Generated by Django 4.2.11 on 2024-04-21 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dust', '0009_alter_health_time_alter_indoorair_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 22, 37, 28, 308342)),
        ),
        migrations.AlterField(
            model_name='indoorair',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 22, 37, 28, 306409)),
        ),
        migrations.AlterField(
            model_name='outdoorair',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 22, 37, 28, 108068)),
        ),
    ]
