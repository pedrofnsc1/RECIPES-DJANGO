from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'base.html', context={
        'message': 'This is your home now'
    })


def sobre(request):
    return HttpResponse('Hello, Sobre!!')


def contato(request):
    return HttpResponse('Hello, Contato!!')
