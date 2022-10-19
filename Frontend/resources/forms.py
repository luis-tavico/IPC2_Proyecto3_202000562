from cProfile import label
from django import forms

class Form(forms.Form):
    id = forms.CharField(label='id')
    nombre = forms.CharField(label='nombre')
    abreviatura = forms.CharField(label='abreviatura')
    metrica = forms.CharField(label='metrica')
    tipo = forms.CharField(widget=forms.Select)
    valorXhora = forms.CharField(label='valorXhora')

    
class FormCategory(forms.Form):
    id = forms.CharField(label='id')
    tipo = forms.CharField(widget=forms.Select)
    #ruta = forms.CharField(widget=forms.ClearableFileInput)