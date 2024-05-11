
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
    time = timezone.now() - datetime.timedelta(days=days)
    outdoor = OutdoorAir.objects.create(time=time, place=place, pm2_5=100,
                                        temp=33, humidity=40)
    return IndoorAir.objects.create(outdoor=outdoor, time=timezone.now(), pm2_5=pm, place=place,
                                          place_type="house", temp=25)


class HomePageTest(TestCase):
    def test_the_indoorair_show_only_latest_for_each_district(self):
        """
        Test that the homepage only displays the latest IndoorAir object for each district.
        """
        indoor1 = create_indoorAir(1,"Bang_Na", 1)
        indoor2 = create_indoorAir(0,"Bang_Na", 30)
        indoor3 = create_indoorAir(0,"Bang_Rak", 20)
        response = self.client.get(reverse('dust:home'))
        self.assertEqual(response.context['indoor'].count(), 2)

    def test_can_not_see_detail_of_none_exist_data(self):
        """
        Test that user can't go to detail page that not exists
        """
        response = self.client.get(reverse('dust:detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

    def test_automate_predict_data(self):
        """
        Test that when user come to homepage and the data in database is update
        new IndoorAir objects should be created.
        """
        indoor = create_indoorAir(0,"Bang_Na", 25)
        outdoor = OutdoorAir.objects.create(time=timezone.now(), place="Bang_Rak", pm2_5=100,temp=33, humidity=40)
        outdoor = OutdoorAir.objects.create(time=timezone.now(), place="Bang_Kapi", pm2_5=100,temp=33, humidity=40)
        response = self.client.get(reverse('dust:home'))
        self.assertEqual(response.context['indoor'].count(), 3)

    def test_home_page_is_valid_even_not_have_any_data(self):
        """
        Test that when user come to homepage with not have any data must be successful response.
        """
        response = self.client.get(reverse('dust:home'))
        self.assertEqual(response.status_code, 200)

    def test_can_not_go_to_old_detail_page(self):
        """
        Test that when go to old detail page the page should not exist
        """
        indoor2 = create_indoorAir(1, "Bang_Na", 30)
        indoor3 = create_indoorAir(0, "Bang_Na", 20)
        response = self.client.get(reverse('dust:detail', kwargs={'pk': 0}))
        self.assertEqual(response.status_code, 404)

class PredictPageTest(TestCase):
    def test_cannot_go_not_exist_result_page(self):
        """
        Test that cannot go to not exist result page
        """
        response = self.client.get(reverse('dust:result', kwargs={'pk': 999}))
        self.assertRedirects(response, reverse('dust:predict'))

    def test_submiss_form_with_valid_data(self):
        outdoor = OutdoorAir.objects.create(time=timezone.now(), place="Bang_Rak", pm2_5=100,temp=33, humidity=40)
        # Submit form with valid data
        url = reverse('dust:predict')
        data = {'district': 'Bang_Rak', 'place': 'House', 'temperature': 25}
        response = self.client.post(url, data)

        # Assert redirection to result page
        self.assertRedirects(response, reverse('dust:result', kwargs={'pk': 1}))

        indoor_air = IndoorAir.objects.get(pk=1)
        self.assertEqual(indoor_air.temp, 25)
        self.assertEqual(indoor_air.place, 'Bang_Rak')

        self.assertEqual(response.status_code, 302)

    def test_missing_form_fields(self):
        """
        Test that when data missing from form's field will not redirect to result page
        """
        url = reverse('dust:predict')
        response = self.client.post(url, {'temperature': 25})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'predict')

    def test_if_result_is_negative(self):
        """
        Test that when predict result is negative will change the value as 0.
        """
        indoor = create_indoorAir(0, "Bang_Na", -20)
        response = self.client.get(reverse('dust:result', kwargs={'pk': 1}))
        result = response.context['result']
        self.assertEqual(0, result.pm2_5)

    def test_predicted_IndoorAir_quality_ranges(self):
        """
        Test correctness of IndoorAir Quality range.
        """
        indoor1 = create_indoorAir(0, "Bang_Na", 20)
        indoor2 = create_indoorAir(0, "Bang_Bua", 30)
        indoor3 = create_indoorAir(0, "Bang_Rak", 70)
        indoor4 = create_indoorAir(0, "Bang_Kapi", 120)
        indoor5 = create_indoorAir(0, "Bang_Bon", 210)
        response1 = self.client.get(reverse('dust:result', kwargs={'pk': 1}))
        self.assertEqual(response1.context['text'],'Very Good air quality!')
        response2 = self.client.get(reverse('dust:result', kwargs={'pk': 2}))
        self.assertEqual(response2.context['text'], 'Good air quality')
        response3 = self.client.get(reverse('dust:result', kwargs={'pk': 3}))
        self.assertEqual(response3.context['text'], 'Moderate air quality')
        response4 = self.client.get(reverse('dust:result', kwargs={'pk': 4}))
        self.assertEqual(response4.context['text'], 'Unhealthy air quality')
        response5 = self.client.get(reverse('dust:result', kwargs={'pk': 5}))
        self.assertEqual(response5.context['text'], 'Very Unhealthy')



class ApiPageTest(TestCase):
    def test_can_go_to_Api_page(self):
        """
        Test that can go to api page successful.
        """
        response = self.client.get('/home/api')
        self.assertEqual(response.status_code, 200)



