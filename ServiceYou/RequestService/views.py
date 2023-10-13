from django.shortcuts import render
from django.views import View

from django.shortcuts import HttpResponse

from .forms import AccountForm, AccountLogin


def login(request):
    return render(request, 'login.html', {'form': AccountLogin})



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
