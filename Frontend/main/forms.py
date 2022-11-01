from django import forms

class FormPathConfigurations(forms.Form):
    file = forms.FileField()

class FormPathConsumptions(forms.Form):
    file = forms.FileField()