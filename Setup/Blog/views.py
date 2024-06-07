from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, este é o meu blog!")
