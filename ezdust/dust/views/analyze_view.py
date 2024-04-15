import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages
from ..models import OutdoorAir, IndoorAir, Health
import datetime

def AnalyzeView(request):
    # get result's IndoorAir object
    indoor = IndoorAir.objects.all()
    outdoor = OutdoorAir.objects.all()
    health = Health.objects.all()
    #todo: visualize data
    return render(request, 'dust/analyze.html', {'indoor':indoor,'outdoor':outdoor,'health': health})
