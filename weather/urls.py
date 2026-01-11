from django.urls import path
from .views import weather_data_api, home

urlpatterns = [
    path('', home, name='home'),
    path('api/weather/', weather_data_api, name='weather-api'),
]
