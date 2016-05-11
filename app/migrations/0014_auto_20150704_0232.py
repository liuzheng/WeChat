# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20150704_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrcode',
            old_name='timestamp',
            new_name='Date',
        ),
        migrations.AddField(
            model_name='qrcode',
            name='Time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
