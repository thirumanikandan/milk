# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

myModels = [CompanyDetails, DistributorDetails, RouteDetails, AreaDetails, CustomerDetails, ProductCategoryDetails, ProductDetails]
# Register your models here.
admin.site.register(myModels)
admin.site.site_url = '/dashboard'

admin.site.site_header = 'Milk administration'
admin.site.index_title = 'Features area'
admin.site.site_title = 'HTML title from adminsitration'