from django.shortcuts import render, redirect
from .forms import SightingForm
from .models import SightForm, TheoryForm

def index(request):
	return render(request, 'pages/index.html')

def intro(request):
	return render(request, 'pages/intro.html')

def introcases(request):
	return render(request, 'pages/introcases.html')

def introtheories(request):
	return render(request, 'pages/introtheories.html')

def braveneworld(request):
	return render(request, 'pages/brave_new_world.html')

def fermi(request):
	return render(request, 'pages/fermi.html')

def sighting(request):
	if request.method == 'POST':
		form = SightingForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('pages:index')
	else:
		form = SightingForm()
	context = {'form':form}
	return render(request, 'pages/sighting.html', context)

def theory(request):
	if request.method == 'POST':
		form = TheoryForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('pages:index')
	else:
		form = TheoryForm()
		context = {'form':form} 
	return render(request, 'pages/theory.html', context)