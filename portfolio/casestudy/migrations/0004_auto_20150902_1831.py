# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0003_auto_20150902_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casestudy',
            options={'verbose_name_plural': 'case studies'},
        ),
    ]
