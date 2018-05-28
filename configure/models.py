# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#company details
class CompanyDetails(models.Model):
     cin = models.CharField(max_length=150, null=True, blank=True)
     name = models.CharField(max_length=250, null=True, blank=True)
     phone = models.CharField(max_length=50, null=True, blank=True)
     address = models.TextField(null=True, blank=True)
     location = models.CharField(max_length=250, null=True, blank=True)
     state = models.CharField(max_length=250, null=True, blank=True)
     country = models.CharField(max_length=250, null=True, blank=True)
     pin = models.CharField(max_length=10, null=True, blank=True)
     is_active = models.BooleanField(default=True)
     class Meta:
        db_table = 'company_info'
        indexes = [
            models.Index(fields=['name']),
        ]
        ordering = ['name']
     def __str__(self):
        return self.name
     
#distributor details
class DistributorDetails(models.Model):
     name = models.CharField(max_length=250, null=True, blank=True)
     email = models.CharField(max_length=150, null=True, blank=True)
     mobile = models.CharField(max_length=50, null=True, blank=True)
     phone = models.CharField(max_length=50, null=True, blank=True)
     address1 = models.TextField(null=True, blank=True)
     address2 = models.TextField(null=True, blank=True)
     company = models.ForeignKey(CompanyDetails,related_name='distributor_company_id', null=True, blank=True)
     is_active = models.BooleanField(default=True)
     class Meta:
        db_table = 'distributor_info'
        indexes = [
            models.Index(fields=['name']),
            
        ]
        ordering = ['name']
     def __str__(self):
        return self.name
        
#route details
class RouteDetails(models.Model):
     name = models.CharField(max_length=250, null=True, blank=True)
     address = models.TextField(null=True, blank=True)
     is_active = models.BooleanField(default=True)
     class Meta:
        db_table = 'route_info'
        indexes = [
            models.Index(fields=['name']),
            
        ]
        ordering = ['name'] 
     def __str__(self):
        return self.name
     
#area category details
class AreaDetails(models.Model):
     name = models.CharField(max_length=250, null=True, blank=True)
     address = models.TextField(null=True, blank=True)
     pin = models.CharField(max_length=10, null=True, blank=True)
     distributor = models.ForeignKey(DistributorDetails,related_name='area_id', null=True, blank=True)
     route = models.ForeignKey(RouteDetails,related_name='area_route_id', null=True, blank=True)
     is_active = models.BooleanField(default=True)
     class Meta:
        db_table = 'area_info'
        indexes = [
            models.Index(fields=['name']),
            
        ]
        ordering = ['name']
     def __str__(self):
        return self.name
        
#customer details
class CustomerDetails(models.Model):
     name = models.CharField(max_length=250, null=True, blank=True)
     email = models.CharField(max_length=150, null=True, blank=True)
     mobile = models.CharField(max_length=50, null=True, blank=True)
     phone = models.CharField(max_length=50, null=True, blank=True)
     address1 = models.TextField(null=True, blank=True)
     address2 = models.TextField(null=True, blank=True)
     company = models.ForeignKey(CompanyDetails,related_name='customer_company_id', null=True, blank=True)
     area = models.ForeignKey(AreaDetails,related_name='customer_area_id', null=True, blank=True)
     is_active = models.BooleanField(default=True)
     class Meta:
        db_table = 'customer_info'
        indexes = [
            models.Index(fields=['name']),
            
        ]
        ordering = ['name']
     def __str__(self):
        return self.name

#product category details
class ProductCategoryDetails(models.Model):
     name = models.CharField(max_length=250, null=True, blank=True)
     is_active = models.BooleanField(default=True)
     class Meta:
        db_table = 'product_category_info'
        indexes = [
            models.Index(fields=['name']),
            
        ]
        ordering = ['name']
     def __str__(self):
        return self.name
    
#product details
class ProductDetails(models.Model):
     name = models.CharField(max_length=250, null=True, blank=True)
     image_name = models.CharField(max_length=250, null=True, blank=True)
     image_path = models.ImageField(upload_to = '', default = 'no-data.jpg', blank=True, null=True)
     price = models.FloatField(null=True, blank=True)
     quantity =  models.IntegerField(null=True, blank=True )
     category = models.ForeignKey(ProductCategoryDetails,related_name='product_category_id', null=True, blank=True)
     company = models.ForeignKey(CompanyDetails,related_name='product_company_id', null=True, blank=True)
     is_active = models.BooleanField(default=True)
     class Meta:
        db_table = 'product_info'
        indexes = [
            models.Index(fields=['name']),
            
        ]
        ordering = ['name']
     def __str__(self):
        return self.name
        
#order details
class OrderDetails(models.Model):
     name = models.CharField(max_length=250, null=True, blank=True)
     quantity = models.IntegerField(null=True, blank=True )
     order_date = models.DateField(null=True, blank=True)
     from_date = models.DateField(null=True, blank=True)
     to_date = models.DateField(null=True, blank=True)
     price = models.FloatField(null=True, blank=True)
     product = models.ForeignKey(ProductDetails,related_name='order_product_id', null=True, blank=True)
     customer = models.ForeignKey(CustomerDetails,related_name='order_customer_id', null=True, blank=True)
     company = models.ForeignKey(CompanyDetails,related_name='order_company_id', null=True, blank=True)
     is_active = models.BooleanField(default=True)
     class Meta:
        db_table = 'order_info'
        indexes = [
            models.Index(fields=['name']),
            
        ]
        ordering = ['name']
     def __str__(self):
        return self.name
