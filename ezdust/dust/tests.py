
import datetime
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone
from dust.models import IndoorAir, OutdoorAir
from django.urls import reverse
import django.test
from django.contrib.auth.models import User

def create_indoorAir(days, place, pm):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    outdoor = OutdoorAir.objects.create(time=time, place=place, pm2_5=100,
                                        temp=33, humidity=40)
    return IndoorAir.objects.create(outdoor=outdoor, time=timezone.now(), pm2_5=pm, place=place,
                                          place_type="house", temp=25)

class HomePageTest(TestCase):
    def test_the_indoorair_show_only_latest_for_each_district(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        indoor1 = create_indoorAir(2,"Bang_Na", 25)
        indoor2 = create_indoorAir(3,"Bang_Na", 30)

        # self.assertContains()
        self.assertNotEqual(self, indoor2, indoor1)