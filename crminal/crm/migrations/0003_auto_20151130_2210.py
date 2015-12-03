# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20151124_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='company',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 12, 1, 5, 10, 1, 316193, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='source',
            field=models.ForeignKey(blank=True, to='crm.Campaign', help_text=b'How did this contact find out about us?', null=True),
        ),
    ]
