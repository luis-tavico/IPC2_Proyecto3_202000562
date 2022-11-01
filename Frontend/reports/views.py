from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import json
end_point='http://127.0.0.1:5000/'

bills = []

############################ BILLS ############################
def getBills(request):
    global bills
    bills = requests.get(end_point+'facturas')
    bills = bills.content.decode('utf-8')
    bills = json.loads(bills)
    return render(request, 'getBills.html', bills)

def invoiceReport(request, numero):
    global bills
    bls = bills["facturas"]
    for bill in bls:
        if bill["numero"] == numero:
            break
    return redirect('facturas')

def invoiceReport(request, numero):
    numberInvoice = {"numero":numero}
    requests.get(end_point+'factura', json=numberInvoice)   
    return redirect('facturas')