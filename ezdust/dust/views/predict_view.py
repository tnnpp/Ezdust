import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import generic
from ..models import OutdoorAir, IndoorAir, Health
import datetime
from ..forms import PredictForm

def PredictView(request):
    if request.method == 'POST':
        form = PredictForm(request.POST)
        # create outdoor object for using to predict indoor.
        data = form.cleaned_data
        predict_time = datetime.datetime.now()
        latest_outdoor = OutdoorAir.objects.filter(time__lte=predict_time, place=data['place']).order_by(
            '-time').first()
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
        return redirect(reverse('dust:result', args=(result.pk,)))
    return render(request,
        template_name='dust/predict_form.html',
        context={'form': PredictForm}
    )

#
# class PredictView(generic.FormView):
#     """View for get data for predict indoor air quality."""
#     template_name = "dust/predict_form.html"
#     form_class = "PredictForm"
#
#     # def __init__(self, **kwargs):
#     #     super().__init__(kwargs)
#     #     self.result = None
#
#     def form_valid(self, form):
#         # create outdoor object for using to predict indoor.
#         data = form.cleaned_data
#         predict_time = datetime.datetime.now()
#         latest_outdoor = OutdoorAir.objects.filter(time__lte=predict_time, place=data['place']).order_by(
#             '-time').first()
#         predict_data = OutdoorAir.objects.create(
#             time=predict_time,
#             place=data['district'],
#             pm2_5=latest_outdoor.pm2_5,
#             temp=latest_outdoor.temp,
#             humidity=latest_outdoor.humidity
#         )
#         predict_data.save()
#         # predict data
#         # todo : predict data, adding characteristic and number of people.
#         # this is dummy
#         self.result = IndoorAir.objects.create(
#             outdoor=predict_data,
#             time=predict_time,
#             place=data['district'],
#             pm2_5=latest_outdoor.pm2_5,
#             temp=latest_outdoor.temp,
#             humidity=latest_outdoor.humidity
#         )
#         self.result.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         pk = self.result.pk  # Assuming self.object holds the created object
#         # Construct the success URL using reverse_lazy and the obtained pk
#         return reverse_lazy('result', kwargs={'pk': pk})


def PredictResultView(request, pk):
    result = IndoorAir.objects.filter(pk=pk)
    return render(request, 'dust/result.html', {'result': result})
