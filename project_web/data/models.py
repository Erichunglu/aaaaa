from django.db import models
from django.forms import ModelForm
from math import pi
import django.forms as forms


class Input(models.Model):
#    A = models.FloatField(
#        verbose_name=' amplitude (m)', default=False)
#    b = models.FloatField(
#        verbose_name=' damping coefficient (kg/s)', default=0.0)
#    w = models.FloatField(
#        verbose_name=' frequency (1/s)', default=2*pi)
#    T = models.FloatField(
#        verbose_name=' time interval (s)', default=18)
#    my_choices = [("Group 1",[ (1,"Choice 1"), (2, "Choice 2")])]
 #   field = models.ChoiceField(label="OPTION", choices=my_choices)
    StartDate = models.CharField(
        verbose_name=' (yyyy/mm/dd) ', max_length=10, blank=False)
    StartTime = models.CharField(
        verbose_name=' (hh/mm/ss) ', max_length=8, blank=False)
    EndDate  = models.CharField(
        verbose_name=' (yyyy/mm/dd) ', max_length=10, blank=False)
    EndTime = models.CharField(
        verbose_name=' (hh/mm/ss) ', max_length=8, blank=False)



class InputForm(ModelForm):
    class Meta:
        model = Input
	widgets= {
		'StartDate': forms.TextInput(attrs={'placeholder': u'ex:2016-09-15'}),
		'StartTime': forms.TextInput(attrs={'placeholder': u'ex:12:00:00'}),
                'EndDate': forms.TextInput(attrs={'placeholder': u'ex:2016-09-15'}),
                'EndTime': forms.TextInput(attrs={'placeholder': u'ex:12:00:00'}),   

	}

