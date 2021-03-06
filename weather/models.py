from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Report(models.Model):
    
    report_date = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()

    city = models.CharField(max_length=50, validators=[MaxLengthValidator(50)])
    state = models.CharField(max_length=2, validators=[MaxLengthValidator(2)])
    zipcode = models.CharField(max_length=5, validators=[MaxLengthValidator(5), MinLengthValidator(5)])
    
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

    description = models.CharField(max_length=500, null=True, blank=True, validators=[MaxLengthValidator(500)])

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.city} - {self.weather}'
    