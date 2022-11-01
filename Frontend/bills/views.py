from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
from .forms import FormBill
from django.contrib import messages
end_point='http://127.0.0.1:5000/'

####################### BILLS #######################
def generate(request):
    form = FormBill(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post(end_point+'generar', json=data)
            response = response.content.decode('utf-8')
            response = json.loads(response)
            mssg = response["mensaje"]
            messages.add_message(request=request, level=messages.SUCCESS, message=mssg)
            return redirect('generar')
    return render(request, 'generate.html') 