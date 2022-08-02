from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class UserEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': None,
        }

class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'date_of_birth', 'photo')

class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-styling'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-styling'}))

class Registration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
      super(Registration, self).__init__(*args, **kwargs)
      for field in self.fields:
         self.fields[field].widget.attrs['class'] = 'form-styling'
