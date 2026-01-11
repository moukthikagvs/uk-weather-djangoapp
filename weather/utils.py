import requests
from .models import WeatherData

def load_weather_data():
    url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt"
    response = requests.get(url)
    lines = response.text.splitlines()

    for line in lines:
        if line.strip() and line[:4].isdigit():
            year = int(line[:4])
            values = line[5:].split()

            for month, value in enumerate(values, start=1):
                if value != "---":
                    WeatherData.objects.create(
                        year=year,
                        month=month,
                        parameter="Tmax",
                        value=float(value)
                    )
