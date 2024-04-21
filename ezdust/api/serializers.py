from rest_framework import serializers
from .models import OutdoorAirAPI
class OutdoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OutdoorAirAPI
        fields = ('time', 'place', 'pm2_5', 'temp', 'humidity')