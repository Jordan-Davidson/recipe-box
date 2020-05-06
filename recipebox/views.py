from django.shortcuts import render, reverse, HttpResponseRedirect
from recipebox.models import Chef, Recipe
from recipebox.forms import AddRecipeForm, AddAuthorForm

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


def add_author(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    return render(request, html, {'form': form})



def add_recipe(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data['title'],
                author = data['author'],
                description = data['description'],
                time = data['time'],
                instructions = data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))


    form = AddRecipeForm()
    return render(request, html, {'form': form})

