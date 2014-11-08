from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    photo = models.ImageField()
    phone_number = models.TextField()
    vk = models.TextField()
    gender = models.CharField(max_length=140)
    birth_date = models.DateField()
    user = models.OneToOneField(User, unique=True)


class Type(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField()


class Place(models.Model):
    coordinates = models.CharField(max_length=128)
    photo = models.ImageField()
    description = models.CharField(max_length=1024)
    url = models.URLField()


class Event(models.Model):
    time = models.DateTimeField()
    description = models.CharField(max_length=1024, default="")
    type = models.ForeignKey(Type, blank=True, null=True)
    place = models.ForeignKey(Place, blank=True, null=True)
    payment = models.IntegerField()
    user = models.ManyToManyField(User, blank=True, null=True)


class Rating(models.Model):
    votes = models.IntegerField()
    place = models.OneToOneField(Place, primary_key=True)


class Comment(models.Model):
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=2048)
    date = models.DateTimeField()
    event = models.ForeignKey(Event)


class Debt(models.Model):
    quantity = models.IntegerField()
    event = models.ForeignKey(Event)
    user_whom = models.ForeignKey(User, related_name='user_whom')
    user_who = models.ForeignKey(User, related_name='user_who')
