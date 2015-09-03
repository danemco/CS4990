# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=b'200')),
                ('photo', models.ImageField(upload_to=b'items/%Y/%m/%d')),
                ('description', models.TextField()),
                ('casestudy', models.ForeignKey(to='casestudy.CaseStudy')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='casestudy',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
