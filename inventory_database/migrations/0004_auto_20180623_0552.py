# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-23 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_database', '0003_auto_20180623_0548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fac',
            old_name='asignee',
            new_name='assignee',
        ),
    ]
