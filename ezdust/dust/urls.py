from django.urls import path
from . import views


app_name = 'dust'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
  ]
