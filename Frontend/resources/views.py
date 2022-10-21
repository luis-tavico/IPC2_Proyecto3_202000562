from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
from .forms import FormResource
end_point='http://127.0.0.1:5000/'

def getResources(request):
    global resources
    resources = requests.get(end_point+'recursos')
    resources = resources.content.decode('utf-8')
    resources = json.loads(resources)
    #resources = resources['recursos']
    print("----->", resources)
    return render(request, 'getResources.html', resources)
    #return render(request, 'getResources.html', context)


############################ RESOURCEs ############################
def createResource(request):
    form = FormResource(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            resource = requests.post(end_point+'crearRecurso', json=data)
            resource = resource.content.decode('utf-8')
            resource = json.loads(resource)
            return redirect('recursos')
    return render(request, 'createResource.html') 

def editResource(request, id):
    resource = search_resource(id)
    form = FormResource(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            resource = requests.put(end_point+'editarRecurso', json=data) 
            resource = resource.content.decode('utf-8')
            resource = json.loads(resource)
            return redirect('recursos')
    return render(request, 'editResource.html', {"recurso":resource})

def deleteResource(request, id):
    id = {"id":id}
    print(id)
    requests.delete(end_point+'eliminarRecurso', json=id)   
    return redirect('recursos')

def search_resource(id):
    rscs = resources["recursos"]
    for resource in rscs:
        if resource["id"] == id:
            return resource