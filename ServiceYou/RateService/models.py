from django.db import models
from Account.models import User


class Rating(models.Model):
    RatingID = models.CharField(max_length=10, primary_key=True)
    RequestID = models.CharField(max_length=10, default='', null=True, blank=True)  # Temporary until actually implemented
    Client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_ratings', null=True)
    Worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker_ratings', null=True)
    RatingValue = models.IntegerField()
    Comments = models.TextField()

    def __str__(self):
        return self.RatingID
