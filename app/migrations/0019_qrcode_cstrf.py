# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20150704_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='cstrf',
            field=models.TextField(null=True),
        ),
    ]
