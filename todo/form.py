from django import forms
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# User = get_user_model()

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['Name', 'Due_Date']

class userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']