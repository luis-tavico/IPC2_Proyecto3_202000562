from django import forms

class FormPathConfigurations(forms.Form):
    ruta = forms.CharField(label='ruta')

class FormPathConsumptions(forms.Form):
    ruta = forms.CharField(label='ruta')