# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-02 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_database', '0006_employee_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab_classroom',
            name='slug',
            field=models.SlugField(default='Test'),
            preserve_default=False,
        ),
    ]
