from django import forms

class FormCategory(forms.Form):
    id = forms.CharField(label='id')
    nombre = forms.CharField(label='nombre')
    descripcion = forms.CharField(label='descripcion')
    cargaTrabajo = forms.CharField(label='cargaTrabajo')

class FormConfiguration(forms.Form):
    id = forms.CharField(label='id')
    nombre = forms.CharField(label='nombre')
    descripcion = forms.CharField(label='descripcion')

class FormResource(forms.Form):
    id = forms.CharField(label='id')
    cantidad = forms.CharField(label='cantidad')
