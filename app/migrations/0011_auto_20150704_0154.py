# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150703_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
