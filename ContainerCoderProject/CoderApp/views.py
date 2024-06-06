from django.shortcuts import render, HttpResponse
from .models import Curso, Profesor, Estudiante, Entregable
from .forms import CursoFormulario, ProfesorFormulario, EntregableFormulario, EstudianteFormulario

#view para el inicio
def inicio(req):

    return render(req, 'inicio.html')

def cursos(req):

    lista = Curso.objects.all()

    return render(req, 'cursos.html', {"lista_cursos": lista})

#formulario Curso
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
    

#formulario Profesor
def formProfesor(req):

    if req.method == 'POST':

        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            nuevo_profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            nuevo_profesor.save()
            #nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            #nuevo_curso.save()
            
            return render(req, 'inicio.html', {"message": "Profesor creado con éxito"})
        else:
            return render(req, 'inicio.html', {"message": "Datos no validos"})
    else:

        miFormulario = ProfesorFormulario()

        return render(req, 'profesor_formulario.html', {"miFormulario": miFormulario})
    

#formulario Estudiante
def formEstudiante(req):

    if req.method == 'POST':

        miFormulario = EstudianteFormulario(req.POST)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            nuevo_estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            nuevo_estudiante.save()
            
            
            return render(req, 'inicio.html', {"message": "Estudiante creado con éxito"})
        else:
            return render(req, 'inicio.html', {"message": "Datos no validos"})
    else:

        miFormulario = EstudianteFormulario()

        return render(req, 'estudiante_formulario.html', {"miFormulario": miFormulario})
    

#formulario Entregable
def formEntregable(req):

    if req.method == 'POST':

        miFormulario = EntregableFormulario(req.POST)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            nuevo_entregable = Entregable(nombre=data['nombre'], fechaDeEntrega=data['fecha_entrega'], entregado=data['entregado'])
            nuevo_entregable.save()
            
            
            return render(req, 'inicio.html', {"message": "Entregable creado con éxito"})
        else:
            return render(req, 'inicio.html', {"message": "Datos no validos"})
    else:

        miFormulario = EntregableFormulario()

        return render(req, 'entregable_formulario.html', {"miFormulario": miFormulario})
    


def entregables(req):

    lista = Entregable.objects.all()

    return render(req, 'entregables.html',{"lista_entregables": lista})

def estudiantes (req):

    lista = Estudiante.objects.all()

    return render(req, 'estudiantes.html', {"lista_estudiantes": lista})

def profesores(req):

    lista = Profesor.objects.all()

    return render(req, 'profesores.html', {"lista_profesores": lista})



def busqueda_camada(req):

    return render(req, 'busqueda_camada.html', {})

def busqueda(req):
    try:
        #req.GET["camada"]

        camada = req.GET["camada"]

        curso = Curso.objects.get(camada=camada)

        return render(req, 'resultado_busqueda.html', {"curso": curso, "camada": camada})
    
    except:

        return render(req, 'inicio.html', {"message": "Camada inexistente"})

 





def inicioo(req):

    return HttpResponse('hola estoy probando que funcione')

def hola(req):

    return render(req, 'hola.html')