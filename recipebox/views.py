from django.shortcuts import render
from recipebox.models import Chef, Recipe

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def chef(request, id):
    print(id)
    data = Chef.objects.filter(id=id)[0]
    recipes = Recipe.objects.filter(author=id)
    return render(request, 'chef.html', {'data': data, 'recipes': recipes})

def recipe(request, id):
    data = Recipe.objects.filter(id=id)[0]
    return render(request, 'recipe.html', {'data': data})