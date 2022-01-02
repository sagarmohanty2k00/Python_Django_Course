from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fund(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spendables = models.FloatField()
    savings = models.FloatField()