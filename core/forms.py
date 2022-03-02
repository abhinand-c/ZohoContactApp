from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models


class LoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput({
            'class': 'form-control',
            'placeholder': 'Create Password',
            'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'            # noqa
        }))

    class Meta:
        model = models.User
        fields = ['email', 'password', 'secret']
        widgets = {
            'secret': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Secret'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'phone']
