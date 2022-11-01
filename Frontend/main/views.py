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
    if request.method == 'POST':
        form = FormPathConfigurations(request.POST, request.FILES)
        if form.is_valid():
            name_file = request.FILES['file']
            file_xml = etree.parse(name_file)
            content = etree.tostring(file_xml, encoding='utf8', method='xml')
            response = requests.post(end_point+'archivoConfiguracion', data=content)
            response = response.content.decode('utf-8')
            response = json.loads(response)
            mssg = response["mensaje"]
            messages.add_message(request=request, level=messages.SUCCESS, message=mssg)
            return redirect('inicio')
    else:
        form = FormPathConfigurations()
    return render(request, 'fileConfiguration.html')

def loadFileConsumption(request):
    if request.method == 'POST':
        form = FormPathConsumptions(request.POST, request.FILES)
        if form.is_valid():
            name_file = request.FILES['file']
            file_xml = etree.parse(name_file)
            content = etree.tostring(file_xml, encoding='utf8', method='xml')
            response = requests.post(end_point+'archivoConsumos', data=content)
            response = response.content.decode('utf-8')
            response = json.loads(response)
            mssg = response["mensaje"]
            messages.add_message(request=request, level=messages.SUCCESS, message=mssg)
            return redirect('inicio')
    else:
        form = FormPathConsumptions()
    return render(request, 'fileConsumption.html')

def start(request):
    messages.add_message(request=request, level=messages.SUCCESS, message="hola")
    #requests.delete(end_point+'eliminarRecurso', json=id)   
    return redirect('inicio')
