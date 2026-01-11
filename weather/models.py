from django.db import models

class WeatherData(models.Model):
    region = models.CharField(max_length=40)
    parameter = models.CharField(max_length=40)
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    value = models.FloatField()

    class Meta:
        unique_together = ('region', 'parameter', 'year', 'month')

    def __str__(self):
        return f"{self.region} {self.parameter} {self.year} {self.month}"
