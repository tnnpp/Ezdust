from rest_framework import serializers
from .models import OutdoorAir, IndoorAir

class OutdoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OutdoorAir
        fields = ('time', 'place', 'pm2_5', 'temp', 'humidity')


class IndoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndoorAir
        fields = ('time', 'place','place_type', 'pm2_5', 'temp')