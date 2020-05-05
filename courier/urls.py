from django.contrib import admin
from django.urls import path
from recipebox.urls import urlpatterns as recipe_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += recipe_urls