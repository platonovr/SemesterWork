# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0003_auto_20141109_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.ForeignKey(to='EventApp.Type', blank=True),
        ),
    ]
