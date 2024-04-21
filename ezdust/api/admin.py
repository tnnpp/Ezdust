from django.contrib import admin
from .models import OutdoorAirAPI, IndoorAirAPI
# Register your models here.
admin.site.register(OutdoorAirAPI)
admin.site.register(IndoorAirAPI)
