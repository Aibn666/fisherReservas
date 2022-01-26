from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, "index.html")

def login(request):

    return render(request, 'login.html')

def gestion(request):

    return render(request, 'gestion.html')

def galeria(request):

    return render(request, 'galeria.html')