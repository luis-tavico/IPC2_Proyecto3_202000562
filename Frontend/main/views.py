from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
from lxml import etree
import xml.etree.ElementTree as ET
from .forms import FormPathConfigurations
from .forms import FormPathConsumptions
end_point='http://127.0.0.1:5000/'

def mainMenu(request):
    return render(request, 'mainMenu.html')

def loadFileConfiguration(request):
    form = FormPathConfigurations(request.POST)
    if request.method == "POST":
        if form.is_valid():
            path = form.cleaned_data
            file_xml = etree.parse(path["ruta"])
            content = etree.tostring(file_xml, encoding='utf8', method='xml')
            requests.post(end_point+'archivoConfiguracion', data=content)
            return redirect('recursos')
    return render(request, 'fileConfiguration.html')

def loadFileConsumption(request):
    return render(request, 'fileConsumption.html')