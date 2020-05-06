from django.urls import path
from recipebox import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('addAuthor', views.add_author),
    path('addRecipe', views.add_recipe),
    path('chef/<int:id>', views.chef),
    path('recipe/<int:id>', views.recipe)
]
