from django import forms

class FormCustomer(forms.Form):
    nit = forms.CharField(label='id')
    nombre = forms.CharField(label='nombre')
    direccion = forms.CharField(label='direccion')
    correoElectronico = forms.CharField(label='correoElectronico')
    usuario = forms.CharField(label='usuario')
    clave = forms.CharField(label='clave')

class FormInstance(forms.Form):
    id = forms.CharField(label='id')
    idConfiguracion = forms.CharField(label='idConfiguracion')
    nombre = forms.CharField(label='nombre')
    fechaInicio = forms.CharField(label='fechaInicio')
    estado = forms.CharField(label='estado')
    fechaFinal = forms.CharField(label='fechaFinal')