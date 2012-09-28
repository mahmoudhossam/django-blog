from django import forms
from models import Post

class SignupForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, max_length=40)
    email = forms.EmailField()

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['created_at']