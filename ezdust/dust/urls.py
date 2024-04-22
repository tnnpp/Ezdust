from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'dust'
router = routers.DefaultRouter()
router.register(r'Outdoor air', views.OutdoorViewSet)
urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('api', include(router.urls)),
    path('<int:pk>', views.HomeDetail, name='detail'),
    path('search', views.SearchBar, name='search'),
    path('predict', views.PredictView, name='predict'),
    path('predict/result/<int:pk>', views.PredictResultView, name='result'),
    path('analyze', views.AnalyzeView, name='analyze'),
    path('indoormode', views.ToggleSwitch, name='indoormode')
  ]
