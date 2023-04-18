from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=False, unique=True)

    def __str__(self):
        return self.user.username

admin.site.register(Coordinator)