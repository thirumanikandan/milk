# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-23 03:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmployeeInfo',
        ),
        migrations.DeleteModel(
            name='SampleInfo',
        ),
        migrations.DeleteModel(
            name='TestInfo',
        ),
    ]
