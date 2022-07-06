from django.shortcuts import render, HttpResponse
#Função request para mostrar na tela
def hello(request,nome,idade):
    return HttpResponse(f'<h1>hello {nome} você tem {idade} anos<h1>')

def soma(request, numero1=10,numero2=20):
    return HttpResponse(f'<h1>Valor 1 = {numero1} \n valor 2 = {numero2} \n Soma = {numero1+numero2}</h1>')

def multiplica(request, numero1=10,numero2=20):
    return HttpResponse(f'<h1>Valor 1 = {numero1} \n valor 2 = {numero2} \n Multiplicação = {numero1*numero2}</h1>')

def divisao(request, numero1=10,numero2=20):
    return HttpResponse(f'<h1>Valor 1 = {numero1} \n valor 2 = {numero2} \n Divisão = {numero1/numero2}</h1>')

# Create your views here.
