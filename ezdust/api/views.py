from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OutdoorSerializer
from .models import OutdoorAirAPI
import requests
# Create your views here.
bangkok_district_boundaries= {
    "Bang_Bon": [13.6592, 100.3991],
    "Bang_Kapi": [13.765833, 100.647778],
    "Bang_Khae": [13.696111, 100.409444],
    "Bang_Khen": [13.873889, 100.596389],
    "Bang_Kho_Laem": [13.693333, 100.5025],
    "Bang_Khun_Thian": [13.660833, 100.435833],
    "Bang_Na": [13.680081, 100.5918],
    "Bang_Phlat": [13.793889, 100.505],
    "Bang_Rak": [13.730833, 100.524167],
    "Bang_Sue": [13.809722, 100.537222],
    "Bangkok_Noi": [13.770867, 100.467933],
    "Bangkok_Yai": [13.722778, 100.476389],
    "Bueng_Kum": [13.785278, 100.669167],
    "Chatuchak": [13.828611, 100.559722],
    "Chom_Thong": [13.677222, 100.484722],
    "Din_Daeng": [13.769722, 100.552778],
    "Don_Mueang": [13.913611, 100.589722],
    "Dusit": [13.776944, 100.520556],
    "Huai_Khwang": [13.776667, 100.579444],
    "Khan_Na_Yao": [13.8271, 100.6743],
    "Khlong_Sam_Wa": [13.859722, 100.704167],
    "Khlong_San": [13.730278, 100.509722],
    "Khlong_Toei": [13.708056, 100.583889],
    "Lak_Si": [13.8875, 100.578889],
    "Lat_Krabang": [13.722317, 100.759669],
    "Lat_Phrao": [13.803611, 100.6075],
    "Min_Buri": [13.813889, 100.748056],
    "Nong_Chok": [13.855556, 100.8625],
    "Nong_Khaem": [13.704722, 100.348889],
    "Pathum_Wan": [13.744942, 100.5222],
    "Phasi_Charoen": [13.714722, 100.437222],
    "Phaya_Thai": [13.78, 100.542778],
    "Phra_Khanong": [13.702222, 100.601667],
    "Phra_Nakhon": [13.764444, 100.499167],
    "Pom_Prap Sattru Phai": [13.758056, 100.513056],
    "Prawet": [13.716944, 100.694444],
    "Rat_Burana": [13.682222, 100.505556],
    "Ratchathewi": [13.758889, 100.534444],
    "Sai_Mai": [13.919167, 100.645833],
    "Samphanthawong": [13.731389, 100.514167],
    "Saphan_Sung": [13.77, 100.684722],
    "Sathon": [13.708056, 100.526389],
    "Suan_Luang": [13.730278, 100.651389],
    "Taling_Chan": [13.776944, 100.456667],
    "Thawi_Watthana": [13.7878, 100.3638],
    "Thon_Buri": [13.725, 100.485833],
    "Thung_Khru": [13.6472, 100.4958],
    "Wang_Thonglang": [13.7864, 100.6087],
    "Watthana": [13.742222, 100.585833],
    "Yan_Nawa": [13.696944, 100.543056]
}
class OutdoorViewSet(viewsets.ModelViewSet):
    queryset = OutdoorAirAPI.objects.all().order_by('time')
    serializer_class = OutdoorSerializer



