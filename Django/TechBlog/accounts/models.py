from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # social media
    github = models.CharField(max_length=255, unique=True, null=True)
    instagram = models.CharField(max_length=255, unique=True, null=True)
    linkedin = models.CharField(max_length=255, unique=True, null=True)

    # other personal info
    address = models.TextField(null=True)
    organization = models.CharField(max_length=200, null=True)