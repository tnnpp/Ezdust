# Generated by Django 4.2.4 on 2024-04-12 08:19

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2024, 4, 12, 15, 19, 0, 940390))),
                ('patient_number', models.IntegerField()),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OutdoorAir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2024, 4, 12, 15, 19, 0, 828390))),
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
                ('time', models.DateTimeField(default=datetime.datetime(2024, 4, 12, 15, 19, 0, 939391))),
                ('characteristic', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('place', models.CharField(max_length=200)),
                ('pm2_5', models.IntegerField()),
                ('temp', models.FloatField()),
                ('humidity', models.FloatField()),
                ('outdoor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dust.indoorair')),
            ],
        ),
    ]
