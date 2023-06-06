from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def nuestros_servicios(request):
    return render(request, 'app/nuestros_servicios.html')

def quienes_somos(request):
    return render(request, 'app/quienes_somos.html')   

def contactanos(request):
    return render(request, 'app/contactanos.html') 


