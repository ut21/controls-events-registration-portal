from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=100)
    coordinator= models.OneToOneField(User, on_delete=models.CASCADE)
    coordinator_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"