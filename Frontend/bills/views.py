from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
#from .forms import FormCategory, FormConfiguration, FormResource
end_point='http://127.0.0.1:5000/'

####################### BILLS #######################
def createInvoice(request):
    """global categories
    categories = requests.get(end_point+'categorias')
    categories = categories.content.decode('utf-8')
    categories = json.loads(categories)
    print("--------->", categories)"""
    #return render(request, 'getCategories.html', categories)
    return render(request, 'createInvoice.html')