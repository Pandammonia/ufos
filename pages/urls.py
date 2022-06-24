from django.contrib import admin
from django.urls import path, include
from . import views 
app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('intro/', views.intro, name='intro'),
    path('intro/cases/', views.introcases, name='introcases'),
    path('intro/theories/', views.introtheories, name='introtheories'),
    path('intro/brave_new_world/', views.braveneworld, name='brave_new_world'),
    path('sighting/', views.sighting, name='sighting'),
    path('fermi/', views.fermi, name='fermi'),
    path('theory/', views.theory, name='theory'),
]
