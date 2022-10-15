from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from lxml import etree
import xml.etree.ElementTree as ET
from .forms import Form
end_point='http://127.0.0.1:5000/'

def mainMenu(request):
    return render(request, 'mainMenu.html')

def loadFileConfiguration(request):
    form = Form(request.POST)
    if request.method == "POST":
        if form.is_valid():
            path = form.cleaned_data
            print(path["ruta"])
            file_xml = etree.parse(path["ruta"])
            content = etree.tostring(file_xml, encoding='utf8', method='xml')
            content = {"contenido":content}
            print(content)
            #resource = requests.post(end_point+'nuevoRecurso', json=content)
            #resource = resource.content.decode('utf-8')
            #resource = json.loads(resource)
            #return redirect('recursos')
    return render(request, 'fileConfiguration.html')

def loadFileConsumption(request):
    return render(request, 'fileConsumption.html')