import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse
from ..models import OutdoorAir, IndoorAir
import datetime
from django.db.models import Q, Count
import joblib
import pandas as pd
import os
from django.conf import settings
from matplotlib import pyplot as plt
import io
import base64


#load predict model
model_path = os.path.join(settings.BASE_DIR, 'dust/static/dust/model/indoorair_model.joblib')
scaler_path = os.path.join(settings.BASE_DIR, 'dust/static/dust/model/scaler.joblib')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

bangkok_districts = {
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
    "Pom_Prap_Sattru_Phai": [13.758056, 100.513056],
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


districts_json = json.dumps(bangkok_districts)


def get_queryset(object):
    """
    Return latest time of IndoorAir of each place in bangkok
    """
    query = Q()
    for i in bangkok_districts.keys():
        latest = object.objects.filter(time__lte=datetime.datetime.now(), place=i).order_by(
            '-time').first()
        if latest:
            query |= Q(pk=latest.pk)
    return object.objects.filter(query)


def district_pm(indoor):
    """
    Return list of indoor and out door pm
    """
    indoor_list = []
    outdoor_list = []

    for j in bangkok_districts.keys():
        in_pm = -1
        out_pm = -1
        for i in indoor:
            if j == i.place:
                in_pm = i.pm2_5
                out_pm = i.outdoor.pm2_5
        indoor_list.append(in_pm)
        outdoor_list.append(out_pm)
    return outdoor_list, indoor_list

def get_query_pk(indoor):
    pk_list = []
    for j in bangkok_districts.keys():
        pk = 0
        for i in indoor:
            if j == i.place:
                pk = i.pk
        pk_list.append(pk)
    return pk_list




def predicted_data():
    """Predict update data"""
    outdoors_with_no_indoors = OutdoorAir.objects.annotate(num_indoorairs=Count('indoorair')).filter(num_indoorairs=0)
    if outdoors_with_no_indoors:
        for i in outdoors_with_no_indoors:
            # predict model
            # discritize time in to 5 category
            if 0 < i.time.hour <= 6:
                time = 2
            elif 6 < i.time.hour <= 12:
                time = 3
            elif 12 < i.time.hour <= 18:
                time = 1
            else:
                time = 0
            new_data = pd.DataFrame({
                'time_category':[time],
                'outdoor_temp': [i.temp],
                'outdoor_humidity': [i.humidity],
                'outdoor_pm2_5' : [i.pm2_5],
                'temp': ['25']
            })
            new_data_scaled = scaler.transform(new_data)
            predicted = model.predict(new_data_scaled)
            if predicted[0] < 0:
                predicted[0] = 0
            # end
            new_indoor = IndoorAir.objects.create(
                outdoor=i,
                time=i.time,
                place=i.place,
                pm2_5=predicted[0],
                place_type='house',
                temp=25
            )


def HomePageView(request):
    """View for the home page displaying data of air quality in each district in bangkok."""
    predicted_data()
    indoor = get_queryset(IndoorAir)
    outdoor_list, indoor_list = district_pm(indoor)
    qpk = get_query_pk(indoor)

    return render(request, 'dust/home_page.html', {'query_pk':qpk,'district': districts_json, 'indoor': indoor, 'pm': outdoor_list, 'mode':'outdoor'})


def HomeDetail(request, pk):
    # get choosed indoor objects
    predicted_data()
    indoors = get_queryset(IndoorAir)
    outdoor_list, indoor_list = district_pm(indoors)
    qpk = get_query_pk(indoors)
    indoor = get_object_or_404(IndoorAir,pk=pk)
    if indoor not in indoors:
        return HttpResponseNotFound()
    # Generate a plot for the IndoorAir data
    data = IndoorAir.objects.filter(place=indoor.place)
    times = [d.time for d in data]
    indoor_value = [d.pm2_5 for d in data]
    outdoor_value = [d.outdoor.pm2_5 for d in data]

    plt.figure(figsize=(5, 3))

    plt.plot(times, indoor_value, label=f'Indoor predict for {indoor.place}', color='blue')
    plt.plot(times, outdoor_value, label=f'Outdoor Data for {indoor.place}', color='red')
    plt.title('Indoor Air Data Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.tick_params(axis='x', which='major', labelsize=6)
    plt.grid(True)
    plt.legend()

    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Convert buffer to Django File and save or directly encode to base64
    image_data = buffer.getvalue()
    base64_encoded_result = base64.b64encode(image_data).decode('utf-8')
    image_url = f"data:image/png;base64,{base64_encoded_result}"

    return render(request, 'dust/home_detail.html', {'query_pk':qpk, 'district': districts_json, 'indoor': indoor, 'pm': outdoor_list, 'mode':'outdoor', 'graph_image_url': image_url})

def SearchBar(request):
    predicted_data()
    indoor = get_queryset(IndoorAir)
    outdoor_list, indoor_list = district_pm(indoor)
    qpk = get_query_pk(indoor)
    if request.method == 'POST':
        query = request.POST.get('query', '')
        results = indoor.filter(place__contains=query)
    return render(request, 'dust/home_page.html', {'query_pk':qpk, 'district': districts_json, 'indoor': results, 'pm': outdoor_list, 'mode':'outdoor'})

def ToggleSwitch(request):
    indoor = get_queryset(IndoorAir)
    outdoor_list, indoor_list = district_pm(indoor)
    qpk = get_query_pk(indoor)
    if request.method == 'POST':
        is_switch = 'switch' in request.POST
        if is_switch:
            return render(request, 'dust/home_page.html',
                          {'query_pk':qpk, 'district': districts_json, 'indoor': indoor, 'pm': indoor_list, 'mode': 'indoor'})
    return redirect(reverse('dust:home'))
