from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from recipebox.models import Chef, Recipe
from recipebox.forms import AddRecipeForm, AddAuthorForm, LoginUserForm

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def chef(request, id):
    data = Chef.objects.filter(id=id)[0]
    recipes = Recipe.objects.filter(author=id)
    return render(request, 'chef.html', {'data': data, 'recipes': recipes})


def recipe(request, id):
    data = Recipe.objects.filter(id=id)[0]
    return render(request, 'recipe.html', {'data': data})

@staff_member_required
def add_author(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            chef = Chef.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=user
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddAuthorForm()
    return render(request, html, {'form': form})


@login_required
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
            return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))


    form = AddRecipeForm()
    return render(request, html, {'form': form})


def loginUser(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginUserForm
    return render(request, html, {'form': form})


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))