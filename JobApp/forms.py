# coding=utf-8
from django import forms
from JobApp.models import Task
from django.utils.translation import ugettext_lazy as _


__author__ = 'roman'


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['hours'].label = 'Оценка (в часах)'
        self.fields['name'].label = 'Название задачи'
        self.fields['description'].label = 'Что нужно сделать?'
        self.fields['user'].label = 'Исполнитель'
        self.fields['critical_hours'].label = 'Объективное количество часов , за которое задача должна быть выполнена'

    class Meta:
        model = Task