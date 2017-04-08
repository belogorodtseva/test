from django.db import models
from datetime import date
from datetime import datetime
from django.core.exceptions import ValidationError
#### appointment #####

class Date(models.Model):
    date = models.DateField(default=date.today)

    def clean(self):
        " Make sure date not in the past "
        if self.date < date.today():
            raise ValidationError('Date cannot be in the past.')

    def __str__(self):
        return str(self.date)


class Time(models.Model):
    time_start = models.TimeField(auto_now=False)
    time_end = models.TimeField(auto_now=False)


    def __str__(self):
        return '%s - %s' % (str(self.time_start), str(self.time_end))


class App(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    date = models.ForeignKey(Date, blank=False)
    time = models.ForeignKey(Time , blank=False)

    def __str__(self):
        return self.name
