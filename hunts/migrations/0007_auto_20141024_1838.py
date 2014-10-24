# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0006_treasurehunt_entryfee'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertreasurehunt',
            name='address',
            field=models.CharField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertreasurehunt',
            name='paid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
