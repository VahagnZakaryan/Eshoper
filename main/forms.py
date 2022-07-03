from xml.etree.ElementTree import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

# Create your forms here.

class NewUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # count = forms.IntegerField(label='count', widget=forms.NumberInput(attrs={'class': 'form-control input-number'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CommentForm(forms.Form):
    com= forms.TextInput()

