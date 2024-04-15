from django.urls import path
from . import views


app_name = 'dust'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('predict', views.PredictView, name='predict'),
    path('predict/result/<int:pk>', views.PredictResultView, name='result')
  ]
