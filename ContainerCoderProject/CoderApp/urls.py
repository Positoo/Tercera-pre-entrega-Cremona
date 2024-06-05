
#from django.contrib import admin
from django.urls import path
from CoderApp.views import (
    inicio,
    cursos,
    formCurso,
    entregables,
    estudiantes,
    profesores,
    busqueda_camada,
    busqueda
)


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('curso-formulario/', formCurso, name='FormCurso'),
    path('entregables/', entregables, name='Entregables'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('profesores/', profesores, name='Profesores'),
    path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    path('busqueda/', busqueda, name='BusquedaCurso'),
]
