# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-06 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0039_auto_20170406_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hdxexportregion',
            name='dataset_prefix',
        ),
    ]