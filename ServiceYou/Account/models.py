from django.db import models


# Create your models here.


class User(models.Model):
    Username = models.CharField(max_length=10, primary_key=True, null=False)
    Password = models.CharField(max_length=20, null=False)
    FirstName = models.CharField(max_length=30, null=False)
    LastName = models.CharField(max_length=30, null=False)
    MiddleName = models.CharField(max_length=30)
    PhoneNo = models.CharField(max_length=11, null=False)
    Email = models.EmailField()
    Address = models.TextField()


class Client(User):
    ClientID = models.CharField(max_length=10, primary_key=True, null=False)

    def __str__(self):
        return self.ClientID


class Worker(User):
    WorkerID = models.CharField(max_length=10, primary_key=True, null=False)
    Status = models.BooleanField()

    def __str__(self):
        return self.WorkerID


class Service(models.Model):
    ServiceID = models.CharField(max_length=10, primary_key=True, null=False)
    WorkerID = models.ForeignKey(Worker, on_delete=models.CASCADE)
    ServiceType = models.CharField(max_length=100)

    def __str__(self):
        return self.ServiceID

    class Meta:
        unique_together = ["WorkerID", "ServiceType"]