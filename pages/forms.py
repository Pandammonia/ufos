from django import forms
from .models import Sighting
class SightingForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(SightingForm, self).__init__(*args, **kwargs)
		self.fields['subj'].label = "Summary of sighting"
		self.fields['body'].label = "Details of sighting"
		self.fields['location'].label = "Location of sighting"
	class Meta:
		model = Sighting
		fields = ['subj', 'body', 'location', 'time_of']



