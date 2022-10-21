from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
#from .forms import FormResource
end_point='http://127.0.0.1:5000/'

consumptions = ""

def getConsumptions(request):
    global consumptions
    #consumptions = requests.get(end_point+'consumos')
    #consumptions = consumptions.content.decode('utf-8')
    #consumptions = json.loads(consumptions)
    #print("----->", consumptions)
    #return render(request, 'getConsumptions.html', consumptions)
    return render(request, 'getConsumptions.html')