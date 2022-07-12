from django.http import Http404
from django.shortcuts import get_list_or_404, render
# from utils.recipes.factory import make_recipe

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    informations = {
        'recipes': recipes
    }
    return render(request, 'recipes/pages/home.html', informations)


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id, 
    #     is_published=True
    # ).order_by('-id')
   
    # if not recipes:
    #     raise Http404("Page Not Found 😒")

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, 
            is_published=True
        ).order_by('-id')
    )
    informations = {
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Categoria |',
    }
    return render(request, 'recipes/pages/category.html', informations)


def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id, 
        is_published=True
    ).order_by('-id').first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
