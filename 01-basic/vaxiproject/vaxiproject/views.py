from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def test(request):
    return HttpResponse('<h1>Bienvenidos a Falconsolutions.com</h1>')