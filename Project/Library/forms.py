from django import forms
from .models import User


class UserModel2Form(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
