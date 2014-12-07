from django import forms

__author__ = 'roman'


class TaskForm(forms.Form):
    hours = forms.IntegerField()
    name = forms.CharField(max_length=128)
    description = forms.CharField(max_length=1024)
