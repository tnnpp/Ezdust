from rest_framework import serializers
from .models import OutdoorAir
class OutdoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OutdoorAir
        fields = ('time', 'place', 'pm2_5', 'temp', 'humidity')