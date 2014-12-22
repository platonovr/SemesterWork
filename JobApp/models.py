from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Fact(models.Model):
    time = models.DateTimeField()
    type = models.BooleanField(default=None)
    user = models.ForeignKey(User)


class Task(models.Model):
    hours = models.IntegerField()
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    user = models.ForeignKey(User)
    critical_hours = models.IntegerField(default=40)


class Bill(models.Model):
    description = models.CharField(max_length=1024)
    end_date = models.DateField()
    user = models.ForeignKey(User)


class Goal(models.Model):
    description = models.CharField(max_length=1024)
    date_when = models.DateField()
    name = models.TextField(null=True)
    user = models.ForeignKey(User)