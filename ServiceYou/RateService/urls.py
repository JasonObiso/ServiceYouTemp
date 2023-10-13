from django.urls import path
from . import views

urlpatterns = [
    path('rating/', views.RateService.as_view(), name='rating'),
    path('clientreg/', views.RegisterClient.as_view(), name='clientreg'),
    path('clientlog/', views.LoginClient.as_view(), name='clientlog'),
    path('workerreg/', views.RegisterWorker.as_view(), name='workerreg'),
    path('workerlog/', views.LoginWorker.as_view(), name='workerlog'),
    path('', views.rating, name='temp'),
]
