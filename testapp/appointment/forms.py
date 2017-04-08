import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from appointment.models import Date,Time,App
from django.contrib.admin import widgets


class AddDateForm(forms.ModelForm):

    class Meta:
        model=Date
        fields = ('date',)
        widgets = {'date' : SelectDateWidget, }

class AddTimeForm(forms.ModelForm):
    class Meta:
        model=Time
        fields = ('time_start', 'time_end')
        widgets = {'time_start': widgets.AdminTimeWidget(), 'time_end': widgets.AdminTimeWidget()}


class ChooseAppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('date','time','name','email')
        widgets = {'date': forms.RadioSelect(),'time': forms.RadioSelect(),}
