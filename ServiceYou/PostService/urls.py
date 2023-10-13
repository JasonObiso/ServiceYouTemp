from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.PostServiceRegistration.as_view(), name='register'),
    path('', views.register),
]

