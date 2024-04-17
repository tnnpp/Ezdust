from django.urls import path
from . import views


app_name = 'dust'
urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('<int:pk>', views.HomeDetail, name='detail'),
    path('search', views.SearchBar, name='search'),
    path('predict', views.PredictView, name='predict'),
    path('predict/result/<int:pk>', views.PredictResultView, name='result'),
    path('analyze', views.AnalyzeView, name='analyze')
  ]
