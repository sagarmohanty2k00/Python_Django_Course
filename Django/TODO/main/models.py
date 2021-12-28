from django.db import models

class Task(models.Model):
    taskName = models.CharField(max_length=256)
    added_date = models.DateField(auto_now=True)


# ORM - Object Relational Mapper