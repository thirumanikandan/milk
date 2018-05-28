# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-25 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('pin', models.CharField(blank=True, max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'area_info',
            },
        ),
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.CharField(blank=True, max_length=150, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('state', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('pin', models.CharField(blank=True, max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'company_info',
            },
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('address1', models.TextField(blank=True, null=True)),
                ('address2', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'customer_info',
            },
        ),
        migrations.CreateModel(
            name='DistributorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('address1', models.TextField(blank=True, null=True)),
                ('address2', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'distributor_info',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'order_info',
            },
        ),
        migrations.CreateModel(
            name='ProductCategoryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'product_category_info',
            },
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'product_info',
            },
        ),
        migrations.CreateModel(
            name='RouteDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'route_info',
            },
        ),
        migrations.DeleteModel(
            name='EmployeeInfo',
        ),
        migrations.AddIndex(
            model_name='routedetails',
            index=models.Index(fields=['name'], name='route_info_name_d0b570_idx'),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category_id', to='configure.ProductCategoryDetails'),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_company_id', to='configure.CompanyDetails'),
        ),
        migrations.AddIndex(
            model_name='productcategorydetails',
            index=models.Index(fields=['name'], name='product_cat_name_f69921_idx'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_area_id', to='configure.AreaDetails'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_company_id', to='configure.CompanyDetails'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_customer_id', to='configure.CustomerDetails'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_product_id', to='configure.ProductDetails'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_route_id', to='configure.RouteDetails'),
        ),
        migrations.AddField(
            model_name='distributordetails',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='distributor_company_id', to='configure.CompanyDetails'),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_company_id', to='configure.CompanyDetails'),
        ),
        migrations.AddIndex(
            model_name='companydetails',
            index=models.Index(fields=['name'], name='company_inf_name_3ef7ce_idx'),
        ),
        migrations.AddField(
            model_name='areadetails',
            name='distributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_id', to='configure.DistributorDetails'),
        ),
        migrations.AddField(
            model_name='areadetails',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_route_id', to='configure.RouteDetails'),
        ),
        migrations.AddIndex(
            model_name='productdetails',
            index=models.Index(fields=['name'], name='product_inf_name_c15566_idx'),
        ),
        migrations.AddIndex(
            model_name='orderdetails',
            index=models.Index(fields=['name'], name='order_info_name_c187b0_idx'),
        ),
        migrations.AddIndex(
            model_name='distributordetails',
            index=models.Index(fields=['name'], name='distributor_name_d22fd6_idx'),
        ),
        migrations.AddIndex(
            model_name='customerdetails',
            index=models.Index(fields=['name'], name='customer_in_name_37d5a2_idx'),
        ),
        migrations.AddIndex(
            model_name='areadetails',
            index=models.Index(fields=['name'], name='area_info_name_31c5af_idx'),
        ),
    ]
