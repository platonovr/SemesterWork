# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0002_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(to='EventApp.Place', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
