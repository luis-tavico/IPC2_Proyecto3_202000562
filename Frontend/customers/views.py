from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
from .forms import FormCustomer, FormInstance
end_point='http://127.0.0.1:5000/'

nitCustomer = ""
customers = ""
instances = ""

########################## CUSTOMERS ##########################
def getCustomers(request):
    global customers
    customers = requests.get(end_point+'clientes')
    customers = customers.content.decode('utf-8')
    customers = json.loads(customers)
    return render(request, 'getCustomers.html', customers)

def createCustomer(request):
    form = FormCustomer(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            customer = requests.post(end_point+'crearCliente', json=data)
            customer = customer.content.decode('utf-8')
            customer = json.loads(customer)
            return redirect('clientes')
    #return render(request, 'newCustomer.html') 
    return render(request, 'createCustomer.html') 

def editCustomer(request, id):
    customer = search_customer(id)
    form = FormCustomer(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            customer = requests.put(end_point+'editarCliente', json=data) 
            customer = customer.content.decode('utf-8')
            customer = json.loads(customer)
            return redirect('clientes')
    return render(request, 'editCustomer.html', {"cliente":customer})

def deleteCustomer(request, nit):
    nit = {"id":nit}
    print(nit)
    requests.delete(end_point+'eliminarCliente', json=nit)   
    return redirect('clientes')

def search_customer(nit):
    ctm = customers["clientes"]
    for customer in ctm:
        if customer["nit"] == nit:
            return customer

########################## INSTANCES ##########################
def getInstances(request, nit):
    global nitCustomer
    nitCustomer = nit
    nit = {"nitCliente":nit}
    global instances
    instances = requests.post(end_point+'instancias', json=nit)
    instances = instances.content.decode('utf-8')
    instances = json.loads(instances)
    print("----->",instances)
    return render(request, 'getInstances.html', instances)

def createInstance(request):
    form = FormCustomer(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            data["idCliente"] = nitCustomer
            customer = requests.post(end_point+'crearInstancia', json=data)
            customer = customer.content.decode('utf-8')
            customer = json.loads(customer)
            return redirect('instancias/'+nitCustomer)
    return render(request, 'createInstance.html', {"nitCliente":nitCustomer}) 

def editInstance(request, id):
    customer = search_customer(id)
    form = FormCustomer(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            customer = requests.put(end_point+'editarCliente', json=data) 
            customer = customer.content.decode('utf-8')
            customer = json.loads(customer)
            return redirect('clientes')
    return render(request, 'editCustomer.html', {"cliente":customer})

def deleteInstance(request, nit):
    nit = {"id":nit}
    print(nit)
    requests.delete(end_point+'eliminarCliente', json=nit)   
    return redirect('clientes')

def search_instance(nit):
    ctm = customers["clientes"]
    for customer in ctm:
        if customer["nit"] == nit:
            return customer

"""def newCustomer(request):
    form = FormCategory(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print("si")
            data = form.cleaned_data
            print(data)
    return render(request, 'newCategory.html') """