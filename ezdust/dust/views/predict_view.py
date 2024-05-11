import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages
from ..models import OutdoorAir, IndoorAir
import datetime
from ..forms import PredictForm
import os
import joblib
from django.conf import settings
import pandas as pd

model_path = os.path.join(settings.BASE_DIR, 'dust/static/dust/model/indoorair_model.joblib')
scaler_path = os.path.join(settings.BASE_DIR, 'dust/static/dust/model/scaler.joblib')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def PredictView(request):
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            # create outdoor object for using to predict indoor.
            data = form.cleaned_data
            predict_time = datetime.datetime.now()
            latest_outdoor = OutdoorAir.objects.filter(time__lte=predict_time, place=data['district']).order_by(
                '-time').first()

            if latest_outdoor == None:
                messages.error(request, "Don't Have Data for predict in data base")
                return render(request,
                                template_name='dust/predict_form.html',
                                context={'form': PredictForm})

            predict_data = OutdoorAir.objects.create(
                time=predict_time,
                place=data['district'],
                pm2_5=latest_outdoor.pm2_5,
                temp=latest_outdoor.temp,
                humidity=latest_outdoor.humidity
            )
            predict_data.save()

            # predict model
            # discritize time in to 5 category
            if 0 < predict_data.time.hour <= 6:
                time = 2
            elif 6 < predict_data.time.hour <= 12:
                time = 3
            elif 12 < predict_data.time.hour <= 18:
                time = 1
            else:
                time = 0
            new_data = pd.DataFrame({
                'time_category': [time],
                'outdoor_temp': [predict_data.temp],
                'outdoor_humidity': [predict_data.humidity],
                'outdoor_pm2_5': [predict_data.pm2_5],
                'temp': ['25']
            })
            new_data_scaled = scaler.transform(new_data)
            predicted = model.predict(new_data_scaled)
            if predicted[0] < 0:
                predicted[0] = 0

            result = IndoorAir.objects.create(
                outdoor=predict_data,
                time=predict_time,
                place=data['district'],
                place_type=data['place'],
                pm2_5=predicted[0],
                temp=data['temperature'],
            )
            result.save()
            messages.success(request, "Predict your indoor air quality successful")
            return redirect(reverse('dust:result', args=(result.pk,)))
    return render(request,
        template_name='dust/predict_form.html',
        context={'form': PredictForm})



def PredictResultView(request, pk):
    # get result's IndoorAir object
    try:
        result = IndoorAir.objects.get(pk=pk)
        if result.pm2_5 < 0:
            result.pm2_5 = 0
            result.save()
        if result.pm2_5 <= 25:
            text = "Very Good air quality!"
        elif 26 <= result.pm2_5 <= 50:
            text = "Good air quality"
        elif 51 <= result.pm2_5 <= 100:
            text = "Moderate air quality"
        elif 101 <= result.pm2_5 <= 150:
            text = "Unhealthy air quality"
        else:
            text = "Very Unhealthy"
    except:
        text = None
        result = None
        messages.error(request, "Haven't Predict yet.")
        return redirect(reverse('dust:predict'))
    return render(request, 'dust/result.html', {'result': result, 'text': text})
