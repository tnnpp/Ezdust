# Generated by Django 4.2.11 on 2024-04-21 10:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outdoorairapi',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 21, 17, 46, 55, 563996)),
        ),
        migrations.CreateModel(
            name='IndoorAirAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_type', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('pm2_5', models.IntegerField()),
                ('temp', models.FloatField()),
                ('humidity', models.FloatField()),
                ('outdoor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.outdoorairapi')),
            ],
        ),
    ]
