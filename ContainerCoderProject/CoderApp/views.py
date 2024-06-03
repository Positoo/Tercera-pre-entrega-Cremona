from django.shortcuts import render, HttpResponse

#view para el inicio
def inicio(req):

    return render(req, 'inicio.html') #puede que necesite un contexto por mas que se vacio. {}

def inicioo(req):

    return HttpResponse('hola estoy probando que funcione')

def hola(req):

    return render(req, 'hola.html')