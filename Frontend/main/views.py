from django.shortcuts import render
from django.http import HttpResponse

def mainMenu(request):
    return render(request, 'mainMenu.html')

