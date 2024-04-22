from rest_framework import viewsets
from ..serializers import OutdoorSerializer
from ..models import OutdoorAir

class OutdoorViewSet(viewsets.ModelViewSet):
    queryset = OutdoorAir.objects.all().order_by('-time')
    serializer_class = OutdoorSerializer
