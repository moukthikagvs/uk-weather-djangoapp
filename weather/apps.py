from django.apps import AppConfig

class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'

    def ready(self):
        from .models import WeatherData
        if not WeatherData.objects.exists():
            from .utils import load_weather_data
            load_weather_data()
