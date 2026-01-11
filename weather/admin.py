from django.contrib import admin
from .models import WeatherData

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('region', 'parameter', 'year', 'month', 'value')
    list_filter = ('parameter', 'year')
    search_fields = ('region', 'month')
