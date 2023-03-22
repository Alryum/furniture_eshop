from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    city = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        pass
