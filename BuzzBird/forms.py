from BuzzBird.models import PostModel
from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(ModelForm):
    body = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': 'True',
        'placeholder': 'Say anything'
    }))

    class Meta:
        model = PostModel
        fields = ['body']
