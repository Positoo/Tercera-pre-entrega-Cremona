
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
    busqueda,
    formProfesor,
    formEstudiante,
    formEntregable
)


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('curso-formulario/', formCurso, name='FormCurso'),
    path('entregables/', entregables, name='Entregables'),
    path('entregable-formulario/', formEntregable, name='FormEntregable'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('estudiante-formulario/', formEstudiante, name='FormEstudiante'),
    path('profesores/', profesores, name='Profesores'),
    path('profesor-formulario/', formProfesor, name='FormProfesor'),
    path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    path('busqueda/', busqueda, name='BusquedaCurso'),
]
