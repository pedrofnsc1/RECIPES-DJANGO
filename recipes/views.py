from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'message': 'This is your home now'
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'message': 'This is your home now'
    })
