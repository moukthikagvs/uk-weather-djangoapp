from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from .models import WeatherData
from .serializers import WeatherDataSerializer


@api_view(['GET'])
def weather_data_api(request):
   
    queryset = WeatherData.objects.all()

  
    year = request.GET.get('year')
    month = request.GET.get('month')
    parameter = request.GET.get('parameter')
    region = request.GET.get('region')

    if year:
        queryset = queryset.filter(year=year)
    if month:
        queryset = queryset.filter(month=month)
    if parameter:
        queryset = queryset.filter(parameter=parameter)
    if region:
        queryset = queryset.filter(region=region)

    serializer = WeatherDataSerializer(queryset, many=True)
    return Response(serializer.data)


def home(request):
    return render(request, 'weather/home.html')
