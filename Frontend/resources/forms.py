from django import forms

class FormResource(forms.Form):
    id = forms.CharField(label='id')
    nombre = forms.CharField(label='nombre')
    abreviatura = forms.CharField(label='abreviatura')
    metrica = forms.CharField(label='metrica')
    tipo = forms.CharField(widget=forms.Select)
    valorXhora = forms.CharField(label='valorXhora')