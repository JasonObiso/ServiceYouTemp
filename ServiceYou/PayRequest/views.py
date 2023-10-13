from django.shortcuts import render
from django.views import View

from .form import AccountForm
from .form import AccountLogin
from django.shortcuts import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'login.html', {'form': AccountLogin})


# def register(request):
#     return render(request, 'register.html', {'form': AccountForm})


# def post(self, request):
#     client = AccountForm(request.POST)
#     if client.is_valid():
#         client_instance = client.save(commit=False)
#         client_instance.save()
#     return render(request, self.template, {'form': client})

class RegisterClient(View):
    template = 'register.html'

    def get(self, request):
        client = AccountForm()
        return render(request, self.template, {'form': client})

    def post(self, request):
        client = AccountForm(request.POST)
        if client.is_valid():
            client_instance = client.save(commit=False)
            client_instance.save()
        return render(request, self.template, {'form': client})
def request(request):
    return HttpResponse("SUCCESS!")
