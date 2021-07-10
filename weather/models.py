from django.db import models

class Report(models.Model):
    
    report_date = models.DateTimeField(auto_now=True)
    temperature = models.FloatField()

    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    
    class Weather(models.TextChoices):
        SUNNY = 'Sunny'
        PARTLY_CLOUDY = 'Partly cloudy'
        MOSTLY_CLOUDY = 'Mosty cloudy'
        RAIN = 'Rain'
        SNOW = 'Snow'
        SLEET = 'Sleet'
        HAIL = 'Hail'
        THUNDERSTORM = 'Thunderstorm'

    weather = models.CharField(
        max_length=13,
        choices=Weather.choices,
        default=Weather.SUNNY,
    )

    description = models.TextField(max_length=500)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
