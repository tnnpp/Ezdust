import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages
from ..models import OutdoorAir, IndoorAir, Health
import datetime
from ..forms import PredictForm

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
            # predict data
            # todo : predict data, adding characteristic and number of people.
            # this is dummy
            result = IndoorAir.objects.create(
                outdoor=predict_data,
                time=predict_time,
                place=data['district'],
                pm2_5=latest_outdoor.pm2_5,
                temp=latest_outdoor.temp,
                humidity=latest_outdoor.humidity
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
    except:
        result = None
        messages.error(request, "Haven't Predict yet.")
    return render(request, 'dust/result.html', {'result': result})
