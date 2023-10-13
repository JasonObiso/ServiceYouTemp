from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, primary_key=True, null=False)
    password = models.CharField(max_length=20, null=False)

class Client(User):
    firstname = models.CharField(max_length=30, null=False)
    middlename = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, null=False)
    phonenumber = models.CharField(max_length=11, null=False)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.ClientID