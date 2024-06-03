from django.http import HttpResponse
from django.shortcuts import render

def saluda(req):
    
    return HttpResponse("hello word")

def saludaNombre (req, name):

    texto = f"El nombre llegado por parametro es: {name}"
    return HttpResponse(texto)
