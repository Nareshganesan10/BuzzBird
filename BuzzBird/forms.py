from django import forms
from BuzzBird import models

class PostForm(forms.ModelForm):
    attribites={'rows':'3','placeholder':'something'}
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs=attribites)
    )

    class Meta:
        model = models.Post
        fields = ['body']