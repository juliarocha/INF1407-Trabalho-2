from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Manager/home.html')

def segundaPagina(request):
    # processamento antes de mostrar
    # a segunda página
    return render(request, 'Manager/segunda.html')