from django import forms
from recipebox.models import Chef

class AddAuthorForm(forms.ModelForm):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(widget=forms.PasswordInput)
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


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(widget=forms.PasswordInput)