'''
Created on Sep 11, 2018

@author: gris
'''

from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ("username", "email", "password")
        
class UserProfileForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)
    
    class Meta():
        model = UserProfile
        fields = ("portfolio", "picture")

        
        
        