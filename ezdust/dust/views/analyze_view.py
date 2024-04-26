import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages
from ..models import OutdoorAir, IndoorAir, Health
import datetime
import joblib
import pandas as pd
import os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'dust/static/dust/model/indoorair_model.joblib')
scaler_path = os.path.join(settings.BASE_DIR, 'dust/static/dust/model/scaler.joblib')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
def AnalyzeView(request):
    # get result's IndoorAir object
    indoor = IndoorAir.objects.all()
    outdoor = OutdoorAir.objects.all()
    health = Health.objects.all()
    #todo: visualize data
    return render(request, 'dust/analyze.html', {'indoor':indoor,'outdoor':outdoor,'health': health})
