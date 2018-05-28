"""hcms_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import views

urlpatterns = [
               url(r'^login_check/',views.LoginCheck.as_view(),name="login_check"),
               url(r'^company_details/',views.CompanyDetailsCRUD.as_view(),name="company_details"),
               url(r'^distributor_details/',views.DistributorDetailsCRUD.as_view(),name="distributor_details"),
               url(r'^route_details/',views.RouteDetailsCRUD.as_view(),name="route_details"),
               url(r'^area_details/',views.AreaDetailsCRUD.as_view(),name="area_details"),
               url(r'^customer_details/',views.CustomerDetailsCRUD.as_view(),name="customer_details"),
               url(r'^product_category_details/',views.ProductCategoryDetailsCRUD.as_view(),name="product_category_details"),
               url(r'^product_details/',views.ProductDetailsCRUD.as_view(),name="product_details"),
               url(r'^order_details/',views.OrderDetailsCRUD.as_view(),name="order_details"),
]