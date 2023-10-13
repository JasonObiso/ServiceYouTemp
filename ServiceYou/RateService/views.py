from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .form import RateServiceForm, ClientRegisterForm, WorkerRegisterForm, ClientLoginForm, WorkerLoginForm


# Create your views here.

def rating(request):
    return HttpResponse("SUCCESS!")


class RateService(View):
    template = 'rating.html'

    def get(self, request):
        score = RateServiceForm()
        return render(request, self.template, {'form': score})


class RegisterClient(View):
    template = 'clientreg.html'

    def get(self, request):
        client = ClientRegisterForm()
        return render(request, self.template, {'form': client})

    def post(self, request):
        client = ClientRegisterForm(request.POST)
        if client.is_valid():
            client_instance = client.save(commit=False)
            client_instance.save()
        return render(request, self.template, {'form': client})


class RegisterWorker(View):
    template = 'workerreg.html'

    def get(self, request):
        worker = WorkerRegisterForm()
        return render(request, self.template, {'form': worker})


class LoginClient(View):
    template = 'clientlog.html'

    def get(self, request):
        client = ClientLoginForm()
        return render(request, self.template, {'form': client})


class LoginWorker(View):
    template = 'workerlog.html'

    def get(self, request):
        worker = WorkerLoginForm()
        return render(request, self.template, {'form': worker})