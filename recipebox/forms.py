from django import forms
from recipebox.models import Chef

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = [
            'name',
            'bio'
        ]


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length =50)
    author = forms.ModelChoiceField(queryset=Chef.objects.all())
    description = forms.CharField(max_length=30)
    time = forms.CharField(max_length=10)
    instructions = forms.CharField(widget=forms.Textarea)


"""
class Chef(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(null=True)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Chef, on_delete=models.CASCADE)
    description = models.CharField(max_length=30, null=True)
    time = models.CharField(max_length=10, null=True)
    instructions = models.TextField()

    """