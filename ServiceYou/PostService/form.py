from django.forms import ModelForm
from django import forms
from Account.models import Worker


class PostServiceForm(ModelForm):
    # workerID = forms.CharField(label='Worker ID', widget=forms.TextInput)
    # serviceType = forms.CharField(label='Service Type',widget=forms.TextInput)

    workerID = forms.CharField(label='Worker ID')
    serviceType = forms.CharField(label='Service Type')

    class Meta:
        model = Worker
        fields = ['workerID', 'serviceType']
