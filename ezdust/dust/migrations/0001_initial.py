# Generated by Django 5.0.4 on 2024-04-21 17:12

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2024, 4, 22, 0, 12, 49, 359319))),
                ('patient_number', models.IntegerField()),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OutdoorAir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2024, 4, 22, 0, 12, 49, 278318))),
                ('place', models.CharField(max_length=200)),
                ('pm2_5', models.IntegerField()),
                ('temp', models.FloatField()),
                ('humidity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IndoorAir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2024, 4, 22, 0, 12, 49, 278318))),
                ('place', models.CharField(max_length=200)),
                ('pm2_5', models.IntegerField()),
                ('temp', models.FloatField()),
                ('humidity', models.FloatField()),
                ('outdoor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dust.outdoorair')),
            ],
        ),
    ]
