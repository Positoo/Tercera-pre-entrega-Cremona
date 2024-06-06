from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class EstudianteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class EntregableFormulario(forms.Form):

    nombre = forms.CharField()
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()