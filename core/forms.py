from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
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
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Name'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }
