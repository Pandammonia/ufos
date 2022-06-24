from django.db import models
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth import get_user_model

class Sighting(models.Model):
	subj = models.CharField(max_length=100)
	body = models.TextField()
	location = models.CharField(max_length=100)
	added = models.DateTimeField(auto_now_add=True)
	time_of = models.CharField(max_length=100)
	name = models.CharField(max_length=80, blank=True, null=True)

	def __str__(self):
		return self.subj

class SightForm(ModelForm):
	class Meta:
		model = Sighting
		fields = ['subj', 'body', 'location', 'time_of']

class Theory(models.Model):
	Title = models.CharField(max_length=100)
	Subject = models.CharField(max_length=100)
	Details = models.TextField()
	Name = models.CharField(max_length=100, blank=True, null=True)
	added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.Title

class TheoryForm(ModelForm):
	class Meta:
		model = Theory
		fields = ['Title', 'Details', 'Name']
