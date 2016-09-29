from django.db import models
from django.forms import ModelForm
from math import pi
import django.forms as forms


class Input(models.Model):
    StartDate = models.CharField(
        verbose_name=' (yyyy-mm-dd) ', max_length=10, blank=False)
    StartTime = models.CharField(
        verbose_name=' (hh-mm-ss) ', max_length=8, blank=False)
    EndDate  = models.CharField(
        verbose_name=' (yyyy-mm-dd) ', max_length=10, blank=False)
    EndTime = models.CharField(
        verbose_name=' (hh-mm-ss) ', max_length=8, blank=False)



class InputForm(ModelForm):
    class Meta:
        model = Input
	widgets= {
		'StartDate': forms.TextInput(attrs={'placeholder': u'ex:2016-09-15'}),
		'StartTime': forms.TextInput(attrs={'placeholder': u'ex:12:00:00'}),
                'EndDate': forms.TextInput(attrs={'placeholder': u'ex:2016-09-15'}),
                'EndTime': forms.TextInput(attrs={'placeholder': u'ex:12:00:00'}),   

	}

