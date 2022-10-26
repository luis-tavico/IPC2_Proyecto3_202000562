from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
from .forms import FormBill
end_point='http://127.0.0.1:5000/'

####################### BILLS #######################
def generateInvoice(request):
    form = FormBill(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            resource = requests.post(end_point+'generarFactura', json=data)
            resource = resource.content.decode('utf-8')
            resource = json.loads(resource)
            return redirect('generarFactura')
    return render(request, 'createInvoice.html') 