# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20150704_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='timestamp',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
