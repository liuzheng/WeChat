# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150703_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='timestamp',
            field=models.DateField(default=datetime.date(2015, 7, 3), verbose_name=b'date published', blank=True),
        ),
    ]
