# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-25 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configure', '0004_auto_20180525_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='image_path',
            field=models.ImageField(blank=True, default='img/no-data.jpg', null=True, upload_to='img/'),
        ),
    ]
