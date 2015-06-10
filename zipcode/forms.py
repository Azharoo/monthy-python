from django.forms import MultiWidget
from django.forms import SplitDateTimeField  
from django import forms
from zipcode.models import *
        
class CareerForm(forms.ModelForm):
        class Meta:
            model = CareerResume

class ZipForm(forms.Form):
	zipsearch = forms.CharField(label='Enter your zipcode below to find the neighborhood hero in your area.', max_length=5)

class ContactForm(forms.Form):
	name = forms.CharField(label='Name', max_length=50)
	address = forms.CharField(label='Address', max_length=50)
	email = forms.EmailField(label='Email', max_length=50)
	problem = forms.CharField(widget=forms.Textarea, label='Description', max_length=200)


class ContractorScheduleForm(forms.ModelForm):
		start_date = SplitDateTimeField()
		end_date   = SplitDateTimeField()
		
		class Meta:
			model = ContractorSchedule	
