from dataclasses import field, fields
from django import forms
from django.contrib.auth.models import User
from lesapp.models import UserProfile

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model= User
        fields=('username','email','password')
class UserProfileInfo(forms.ModelForm):
    class Meta():
        model= UserProfile
        fields= ('portfolio_site','profile_pic')