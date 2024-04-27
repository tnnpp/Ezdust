from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OutdoorAir

@receiver(post_save, sender=OutdoorAir)
def check(sender, instance, created, **kwargs):
    if created:
        print("A new outdoorAir has been created!")

