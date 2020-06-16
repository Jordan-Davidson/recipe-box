from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Chef, on_delete=models.CASCADE)
    description = models.CharField(max_length=30, null=True)
    time = models.CharField(max_length=10, null=True)
    instructions = models.TextField()

    def __str__(self):
        return self.title