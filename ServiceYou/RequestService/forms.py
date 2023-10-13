from django.forms import ModelForm
from django import forms
from .models import Client

class AccountLogin(ModelForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Client
        fields=['username','password']

class AccountForm(ModelForm):
    ClientID = forms.CharField(widget=forms.TextInput)
    username= forms.CharField()
    password = forms.CharField()
    firstname = forms.CharField()
    middlename = forms.CharField()
    lastname = forms.CharField()
    phonenumber = forms.CharField()
    email = forms.CharField()
    address = forms.CharField()

    class Meta:
        model = Client
        fields=['ClientID','username', 'password','firstname','middlename','lastname','phonenumber','email','address']
