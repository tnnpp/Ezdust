# Generated by Django 5.0.4 on 2024-04-18 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dust', '0005_alter_health_time_alter_indoorair_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 18, 13, 53, 16, 497244)),
        ),
        migrations.AlterField(
            model_name='indoorair',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 18, 13, 53, 16, 494562)),
        ),
        migrations.AlterField(
            model_name='outdoorair',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 18, 13, 53, 16, 321543)),
        ),
    ]
