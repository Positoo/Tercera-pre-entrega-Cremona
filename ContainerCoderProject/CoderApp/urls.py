
#from django.contrib import admin
from django.urls import path
from CoderApp.views import inicio


urlpatterns = [
    path('inicio/', inicio),
]
