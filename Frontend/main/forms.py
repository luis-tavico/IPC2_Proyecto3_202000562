from django import forms

class Form(forms.Form):
    ruta = forms.CharField(label='ruta')