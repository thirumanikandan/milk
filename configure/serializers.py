from django.contrib.auth.models import User
from rest_framework import serializers
#custom models refer
from .models import *

#custom models refer
class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
    	fields = ('id','cin','name','phone','address','location','state','country','pin')

#distributor models refer
class DistributorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributorDetails
        fields = ('id','name','email','mobile','phone','address1','address2')

#route models refer
class RouteDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteDetails
        fields = ('id','name','address')

#area models refer
class AreaDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaDetails
        fields = ('id','name','address','pin')

#customer models refer
class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = ('id','name','email','mobile','phone','address1','address2')

#product category models refer
class ProductCategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryDetails
        fields = ('id','name')
           
#product models refer
class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = ('id','name','image_name','image_path','price','quantity','category','company')
        
#order models refer
class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ('id','name','quantity','order_date','from_date','to_date','price','product','customer','area','route','company')