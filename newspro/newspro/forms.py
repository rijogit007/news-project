from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
# Create your views here.

class UserregisterForm(forms.ModelForm):
    class  Meta:
           model=User
           fields=["first_name","last_name","email","username","password"]
           widgets={
                 
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.TextInput(attrs={'class':'form-control'}),
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.TextInput(attrs={'class':'form-control'}),
        }


class UserLoginForm(forms.ModelForm):
          class  Meta:
           model=User
           fields=["username","password"]
           widgets={
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.TextInput(attrs={'class':'form-control'}),

           }