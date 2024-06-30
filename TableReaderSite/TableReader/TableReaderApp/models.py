from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=63)
    date_registration = models.DateField(auto_now_add=True)
    subscription_end_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.user_name


class ImageModel:
    def __init__(self, image):
        self.image = image
