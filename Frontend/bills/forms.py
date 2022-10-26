from django import forms

class FormBill(forms.Form):
    fechaInicio = forms.CharField(label='fechaInicio')
    fechaFinal = forms.CharField(label='fechaFinal')