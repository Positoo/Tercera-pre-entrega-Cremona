from django.shortcuts import render, HttpResponse
from .models import Curso
from .forms import CursoFormulario

#view para el inicio
def inicio(req):

    return render(req, 'inicio.html')

def cursos(req):

    lista = Curso.objects.all()

    return render(req, 'cursos.html', {"lista_cursos": lista})

def formCurso(req):

    if req.method == 'POST':

        miFormulario = CursoFormulario(req.POST)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
            
            return render(req, 'inicio.html', {"message": "Curso creado con éxito"})
        else:
            return render(req, 'inicio.html', {"message": "Datos no validos"})
    else:

        miFormulario = CursoFormulario()

        return render(req, 'curso_formulario.html', {"miFormulario": miFormulario})



def entregables(req):

    return render(req, 'entregables.html',{})

def estudiantes (req):

    return render(req, 'estudiantes.html', {})

def profesores(req):

    return render(req, 'profesores.html', {})



def busqueda_camada(req):

    return render(req, 'busqueda_camada.html', {})

def busqueda(req):
    if req.GET["camada"]:

        camada = req.GET["camada"]

        curso = Curso.objects.get(camada=camada)

        return render(req, 'resultado_busqueda.html', {"curso": curso, "camada": camada})
    
    else:

        return render(req, 'inicio.html', {"message": "Error en el dato de la camada"})

 





def inicioo(req):

    return HttpResponse('hola estoy probando que funcione')

def hola(req):

    return render(req, 'hola.html')