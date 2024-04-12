from django.contrib import admin
from dust.models import Health, IndoorAir, OutdoorAir

# Register models
admin.site.register(Health)
admin.site.register(IndoorAir)
admin.site.register(OutdoorAir)


