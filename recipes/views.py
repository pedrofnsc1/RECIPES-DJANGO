from django.http import HttpResponse
#from django.shortcuts import render


def my_view(request):
    return HttpResponse('Hello, Home!!')


def sobre(request):
    return HttpResponse('Hello, Sobre!!')


def contato(request):
    return HttpResponse('Hello, Contato!!')
