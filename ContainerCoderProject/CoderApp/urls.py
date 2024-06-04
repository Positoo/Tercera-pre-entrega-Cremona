
#from django.contrib import admin
from django.urls import path
from CoderApp.views import inicio, cursos, entregables, estudiantes, profesores


urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
]
