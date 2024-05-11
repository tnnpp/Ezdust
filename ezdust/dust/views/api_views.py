from rest_framework import viewsets
from ..serializers import IndoorSerializer, OutdoorSerializer
from ..models import IndoorAir, OutdoorAir

class OutdoorViewSet(viewsets.ModelViewSet):
    queryset = OutdoorAir.objects.all()
    serializer_class = OutdoorSerializer

class IndoorViewSet(viewsets.ModelViewSet):
    queryset = IndoorAir.objects.all().order_by('-time')
    serializer_class = IndoorSerializer
