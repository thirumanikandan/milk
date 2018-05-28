# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-23 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('code', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'emp_info',
            },
        ),
        migrations.CreateModel(
            name='SampleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('path', models.CharField(max_length=100, null=True)),
                ('format', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'sample_info',
            },
        ),
        migrations.CreateModel(
            name='TestInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'test_info',
            },
        ),
    ]
