from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    reason = models.TextField()
    date = models.DateField()
    time = models.TimeField()
