# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0002_auto_20150902_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'200')),
                ('image', models.ImageField(upload_to=b'items/%Y/%m/%d')),
                ('description', models.TextField()),
                ('casestudy', models.ForeignKey(to='casestudy.CaseStudy')),
            ],
        ),
        migrations.RemoveField(
            model_name='study',
            name='casestudy',
        ),
        migrations.DeleteModel(
            name='Study',
        ),
    ]
