from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import PostServiceForm


# Create your views here.

def register(request):
    return HttpResponse('Post Service Homepage')


class PostServiceRegistration(View):
    template = 'index.html'

    def get(self, request):
        worker = PostServiceForm()
        return render(request, self.template, {'form': worker})
