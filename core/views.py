from django.shortcuts import render, HttpResponse
#Função request para mostrar na tela
def hello(request, nome,idade):
    return HttpResponse(f'<h1> Hello {nome} de {idade}</h1><button>Apertar</button>')

# Create your views here.
