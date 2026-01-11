import pandas as pd
from django.core.management.base import BaseCommand
from weather.models import WeatherData

BASE_URL = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/date/{region}.txt"

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('parameter', type=str, default='Tmax')
        parser.add_argument('region', type=str, default='UK')

    def handle(self, *args, **kwargs):
        parameter = kwargs['parameter']
        region = kwargs['region']

        url = BASE_URL.format(parameter=parameter, region=region)

        df = pd.read_fwf(url, skiprows=5)
        df.columns = df.columns.astype(str).str.strip()
        df = df.dropna(how='all')

        months = df.columns[1:]

        for _, row in df.iterrows():
            year = int(row.iloc[0])

            for month in months:
                value = row[month]

                if value == '---':
                    continue

                WeatherData.objects.get_or_create(
                    region=region,
                    parameter=parameter,
                    year=year,
                    month=month,
                    value=float(value)
                )

        self.stdout.write(self.style.SUCCESS(
            f"Weather data loaded successfully for {parameter} {region}"
        ))
