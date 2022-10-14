from django import forms

class Form(forms.Form):
    id = forms.CharField(label='id')
    nombre = forms.CharField(label='nombre')
    abreviatura = forms.CharField(label='abreviatura')
    metrica = forms.CharField(label='metrica')
    tipo = forms.CharField(label='tipo')
    valorXhora = forms.CharField(label='valorXhora')