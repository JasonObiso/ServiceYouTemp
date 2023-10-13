from django.forms import ModelForm
from django import forms
from .models import Rating
from Account.models import Client, Worker


class RateServiceForm(ModelForm):
    RatingID = forms.CharField(widget=forms.TextInput)
    ServiceID = forms.CharField(widget=forms.TextInput)
    ClientID = forms.CharField(widget=forms.TextInput)
    WorkerID = forms.CharField(widget=forms.TextInput)
    RatingValue = forms.IntegerField(widget=forms.NumberInput)
    Comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Rating
        fields = ['RatingID', 'ServiceID', 'ClientID', 'WorkerID', 'RatingValue', 'Comments']


class ClientRegisterForm(ModelForm):
    ClientID = forms.CharField(widget=forms.TextInput)
    Username = forms.CharField(widget=forms.TextInput)
    Password = forms.CharField(widget=forms.PasswordInput)
    FirstName = forms.CharField(widget=forms.TextInput)
    LastName = forms.CharField(widget=forms.TextInput)
    MiddleName = forms.CharField(widget=forms.TextInput)
    PhoneNo = forms.CharField(widget=forms.TextInput)
    Email = forms.EmailField(widget=forms.TextInput)
    Address = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Client
        fields = ['Username', 'Password', 'FirstName', 'LastName', 'MiddleName', 'PhoneNo', 'Email', 'Address', 'ClientID']


class WorkerRegisterForm(ModelForm):
    WorkerID = forms.CharField(widget=forms.TextInput)
    Username = forms.CharField(widget=forms.TextInput)
    Password = forms.CharField(widget=forms.PasswordInput)
    FirstName = forms.CharField(widget=forms.TextInput)
    LastName = forms.CharField(widget=forms.TextInput)
    MiddleName = forms.CharField(widget=forms.TextInput)
    PhoneNo = forms.CharField(widget=forms.TextInput)
    Email = forms.EmailField(widget=forms.TextInput)
    Address = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Worker
        fields = ['Username', 'Password', 'FirstName', 'LastName', 'MiddleName', 'PhoneNo', 'Email', 'Address', 'WorkerID']


class ClientLoginForm(ModelForm):
    Username = forms.CharField(widget=forms.TextInput)
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['Username', 'Password']


class WorkerLoginForm(ModelForm):
    Username = forms.CharField(widget=forms.TextInput)
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['Username', 'Password']