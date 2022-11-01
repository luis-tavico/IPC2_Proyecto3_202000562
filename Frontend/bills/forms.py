from django import forms

class FormBill(forms.Form):
    opcion = forms.CharField(widget=forms.Select)
    fechaInicio = forms.CharField(label='fechaInicio')
    fechaFinal = forms.CharField(label='fechaFinal')