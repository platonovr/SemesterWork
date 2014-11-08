# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0004_auto_20141109_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(blank=True, to='EventApp.Place', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.ForeignKey(blank=True, to='EventApp.Type', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
