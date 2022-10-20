from unicodedata import category
from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
from .forms import FormCategory, FormConfiguration
end_point='http://127.0.0.1:5000/'

def getCategories(request):
    global categories
    categories = requests.get(end_point+'categorias')
    categories = categories.content.decode('utf-8')
    categories = json.loads(categories)
    return render(request, 'getCategories.html', categories)

def newCategory(request):
    form = FormCategory(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            category = requests.post(end_point+'nuevaCategoria', json=data)
            category = category.content.decode('utf-8')
            category = json.loads(category)
            return redirect('categorias')
    return render(request, 'newCategory.html') 

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
    return render(request, 'editResource.html', {"categoria":category})

def deleteCategory(request, id):
    id = {"id":id}
    print(id)
    requests.delete(end_point+'eliminarCategoria', json=id)   
    return redirect('categorias')

def search_category(id):
    ctg = categories["categorias"]
    for category in ctg:
        if category["id"] == id:
            return category

"""def newCategory(request):
    form = FormCategory(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print("si")
            data = form.cleaned_data
            print(data)
    return render(request, 'newCategory.html') """

def getConfigurations(request, id):
    global idCategory
    idCategory = id
    id = {"idCategoria":id}
    global configurations
    configurations = requests.post(end_point+'configuraciones', json=id) 
    configurations = configurations.content.decode('utf-8')
    configurations = json.loads(configurations)
    print("----->",configurations)
    return render(request, 'getConfigurations.html', configurations)

def newConfiguration(request):
    form = FormConfiguration(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            data["idCategoria"] = idCategory
            configuration = requests.post(end_point+'nuevaConfiguracion', json=data)
            configuration = configuration.content.decode('utf-8')
            configuration = json.loads(configuration)
            return redirect('configuraciones/'+idCategory)
    return render(request, 'newConfiguration.html', {"idCategoria":idCategory}) 
    #return render(request, 'newResource.html', {'form':form}) 

def editConfiguration(request, id):
    #resource = search_configuration(id)
    form = FormConfiguration(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            configuration = requests.put(end_point+'editarConfiguracion', json=data) 
            configuration = configuration.content.decode('utf-8')
            configuration = json.loads(configuration)
            #return redirect('configuraciones')
    return render(request, 'editConfiguration.html', {"configuracion":configuration})

def deleteConfiguration(request, id):
    id = {"id":id}
    print(id)
    requests.delete(end_point+'eliminarConfiguracion', json=id)   
    return redirect('configuraciones')

def search_category(id):
    pass

def getResources(request):
    global resources
    resources = requests.get(end_point+'configuraciones')
    resources = resources.content.decode('utf-8')
    resources = json.loads(resources)
    return render(request, 'getResources.html', resources)

def newResource(request):
    form = FormCategory(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            resource = requests.post(end_point+'nuevaCategoria', json=data)
            resource = resource.content.decode('utf-8')
            resource = json.loads(resource)
            return redirect('recursos')
    return render(request, 'newResources.html', {'form':form}) 
    #return render(request, 'newResource.html', {'form':form}) 

def editResource(request, id):
    #resource = search_configuration(id)
    form = FormCategory(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            resource = requests.put(end_point+'editarConfiguracion', json=data) 
            resource = resource.content.decode('utf-8')
            resource = json.loads(resource)
            return redirect('recursos')
    return render(request, 'editResource.html', {"configuracion":resource})

def deleteResource(request, id):
    id = {"id":id}
    print(id)
    requests.delete(end_point+'eliminarResource', json=id)   
    return redirect('recursos')