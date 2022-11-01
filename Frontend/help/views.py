from django.shortcuts import redirect, render
import requests
end_point='http://127.0.0.1:5000/'


############################ BILLS ############################
def about(request):
    return render(request, 'about.html')

def document(request): 
    requests.get(end_point+'documentacion')   
    return redirect('inicio')