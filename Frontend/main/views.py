from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
import requests
import json
from lxml import etree
import xml.etree.ElementTree as ET
from .forms import FormPathConfigurations, FormPathConsumptions
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
            response = requests.post(end_point+'archivoConfiguracion', data=content)
            response = response.content.decode('utf-8')
            response = json.loads(response)
            mssg = response["mensaje"]
            messages.add_message(request=request, level=messages.SUCCESS, message=mssg)
            #messages.success(request, f"Agregado")
            return redirect('inicio')
    return render(request, 'fileConfiguration.html')

def loadFileConsumption(request):
    form = FormPathConsumptions(request.POST)
    if request.method == "POST":
        if form.is_valid():
            path = form.cleaned_data
            file_xml = etree.parse(path["ruta"])
            content = etree.tostring(file_xml, encoding='utf8', method='xml')
            response = requests.post(end_point+'archivoConsumos', data=content)
            response = response.content.decode('utf-8')
            response = json.loads(response)
            print(response)
            return redirect('inicio')
    return render(request, 'fileConsumption.html')