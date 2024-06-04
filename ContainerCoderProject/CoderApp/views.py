from django.shortcuts import render, HttpResponse

#view para el inicio
def inicio(req):

    return render(req, 'inicio.html')

def cursos(req):

    return render(req, 'cursos.html')

def entregables(req):

    return render(req, 'entregables.html')

def estudiantes (req):

    return render(req, 'estudiantes.html')

def profesores(req):

    return render(req, 'profesores.html')







def inicioo(req):

    return HttpResponse('hola estoy probando que funcione')

def hola(req):

    return render(req, 'hola.html')