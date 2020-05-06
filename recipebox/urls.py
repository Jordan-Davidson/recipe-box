from django.urls import path
from recipebox import views

urlpatterns = [
    path('', views.index),
    path('chef/<int:id>/', views.chef),
    path('recipe/<int:id>/', views.recipe)
]
