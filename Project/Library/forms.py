from .models import Livros
from django import forms
from .models import User


class UserModel2Form(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class LivrosModel2Form(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
