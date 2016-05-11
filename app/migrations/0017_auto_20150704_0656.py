# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20150704_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
