from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
from .forms import FormCategory, FormConfiguration, FormResource
end_point='http://127.0.0.1:5000/'

idCategory = ""
idConfiguration = ""
categories = ""
configurations = ""
resources = ""

####################### CATEGORIES #######################
def getCategories(request):
    global categories
    categories = requests.get(end_point+'categorias')
    categories = categories.content.decode('utf-8')
    categories = json.loads(categories)
    return render(request, 'getCategories.html', categories)

def createCategory(request):
    form = FormCategory(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            category = requests.post(end_point+'crearCategoria', json=data)
            category = category.content.decode('utf-8')
            category = json.loads(category)
            return redirect('categorias')
    return render(request, 'createCategory.html') 

def editCategory(request, id):
    category = search_category(id)
    form = FormCategory(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            category = requests.put(end_point+'editarCategoria', json=data) 
            category = category.content.decode('utf-8')
            category = json.loads(category)
            return redirect('categorias')
    return render(request, 'editCategory.html', {"categoria":category})

def deleteCategory(request, id):
    id = {"id":id}
    requests.delete(end_point+'eliminarCategoria', json=id)   
    return redirect('categorias')

def search_category(id):
    global categories
    ctgs = categories["categorias"]
    for category in ctgs:
        if category["id"] == id:
            return category

####################### CONFIGURATIONS #######################
def getConfigurations(request, id):
    global idCategory
    idCategory = id
    id = {"idCategoria":id}
    global configurations
    configurations = requests.post(end_point+'configuraciones', json=id) 
    configurations = configurations.content.decode('utf-8')
    configurations = json.loads(configurations)
    return render(request, 'getConfigurations.html', configurations)

def createConfiguration(request):
    global idCategory
    form = FormConfiguration(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            data["idCategoria"] = idCategory
            configuration = requests.post(end_point+'crearConfiguracion', json=data)
            configuration = configuration.content.decode('utf-8')
            configuration = json.loads(configuration)
            return redirect('configuraciones/'+idCategory)
    return render(request, 'createConfiguration.html', {"idCategoria":idCategory}) 
    #return render(request, 'newResource.html', {'form':form}) 

def editConfiguration(request, id):
    global idCategory
    configuration = search_configuration(id)  
    configuration["idCategoria"] = idCategory
    form = FormConfiguration(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            data["idCategoria"] = idCategory
            configuration = requests.put(end_point+'editarConfiguracion', json=data) 
            configuration = configuration.content.decode('utf-8')
            configuration = json.loads(configuration)
            return redirect('configuraciones/'+idCategory)
    return render(request, 'editConfiguration.html', {"configuracion":configuration})

def deleteConfiguration(request, id):
    global idCategory
    data = {}
    data["idConfiguracion"] = id
    data["idCategoria"] = idCategory
    requests.delete(end_point+'eliminarConfiguracion', json=data)   
    return redirect('configuraciones/'+idCategory)

def search_configuration(id):
    global configurations
    cnfs = configurations["configuraciones"]
    for configuration in cnfs:
        if configuration["id"] == id:
            return configuration

####################### RESOURCES #######################
def getResources(request, id):
    global idCategory
    global idConfiguration
    idConfiguration = id
    data = {"idCategoria":idCategory, "idConfiguracion":idConfiguration}
    global resources
    resources = requests.post(end_point+'recursosConfiguracion', json=data) 
    resources = resources.content.decode('utf-8')
    resources = json.loads(resources)
    return render(request, 'getResourcesInConfiguration.html', resources)

def addResource(request):
    form = FormResource(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            data["idCategoria"] = idCategory
            data["idConfiguracion"] = idConfiguration
            resource = requests.post(end_point+'agregarRecursoConfiguracion', json=data)
            resource = resource.content.decode('utf-8')
            resource = json.loads(resource)
            return redirect('recursosEnConfiguracion/'+idConfiguration)
    return render(request, 'addResource.html', {'idConfiguracion':idConfiguration}) 

def editResource(request, id):
    #resource = search_configuration(id)
    form = FormCategory(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            resource = requests.put(end_point+'editarRecursoConfiguracion', json=data) 
            resource = resource.content.decode('utf-8')
            resource = json.loads(resource)
            return redirect('recursosEnConfiguracion/'+idConfiguration)
    return render(request, 'editResource.html', {"recurso":resource})

def deleteResource(request, id):
    global idCategory
    global idConfiguration
    idResource = id
    data = {"idCategoria":idCategory, "idConfiguracion":idConfiguration, "idRecurso":idResource}
    requests.delete(end_point+'eliminarRecursoConfiguracion', json=data)   
    return redirect('recursosEnConfiguracion/'+idConfiguration)