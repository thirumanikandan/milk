from django.contrib.auth.models import User
from rest_framework import viewsets
#custom test models refer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import json
from django.shortcuts import render
#login authenticate
from django.contrib.auth import authenticate, login
from .models import *
from .serializers import *

#login class here
class LoginCheck(APIView):
    def post(self, request):
            try:
               print ("---------POST------",request.body)
               datas = json.loads(request.body);
               print"-----------===========-----",datas['data'][0]['username'],datas['data'][0]['password']
               # your code...
               username = datas['data'][0]['username']
               password = datas['data'][0]['password']
               user = authenticate(username=username, password=password)
               print ("--------------",user)
               if username and password and user is not None:
                      login(request, user)
                      return HttpResponse(json.dumps({'status': 'M1'}))
               return HttpResponse(json.dumps({'status': 'M2'}))
            except Exception as e:
                print (e)
                return HttpResponse(json.dumps({'status': 'M3'}))
            
#Company Details CRUD Opertaion
class CompanyDetailsCRUD(APIView):
    def get(self, request):
        try:
            # your code...
            print ("---------Company Details Get------",request.body)
            queryset = CompanyDetails.objects.filter(is_active = True).all()
            serializer = CompanyDetailsSerializer(queryset,many=True)
            print "==========ss",serializer.data
            return HttpResponse(json.dumps({'data': serializer.data,'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'}))

    def post(self, request):
        try:
            print ("---------Company Details POST------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['name'])
            # your code...
            AddStatus = CompanyDetails(name = str(datas['data'][0]['name']),cin = str(datas['data'][0]['cin']),phone = str(datas['data'][0]['phone']),address = str(datas['data'][0]['address']),location = str(datas['data'][0]['location']),state = str(datas['data'][0]['state']),country = str(datas['data'][0]['country']),pin = str(datas['data'][0]['pin']))
            AddStatus.save()
            if AddStatus.id:
                return HttpResponse(json.dumps({'status': 'M1'}))
            return HttpResponse(json.dumps({'status': 'M2'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'status': 'M3'}))
            
    def put(self, request):
        try:
            # your code...
            print ("---------Company Details Put------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = CompanyDetails.objects.filter(id = int(datas['data'][0]['id'])).update(name = str(datas['data'][0]['name']),cin = str(datas['data'][0]['cin']),phone = str(datas['data'][0]['phone']),address = str(datas['data'][0]['address']),location = str(datas['data'][0]['location']),state = str(datas['data'][0]['state']),country = str(datas['data'][0]['country']),pin = str(datas['data'][0]['pin']))
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'status': 'M3'}))
            
    def delete(self, request):
        try:
            # your code...
            print ("---------Compan yDetails Delete------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = CompanyDetails.objects.filter(id = int(datas['data'][0]['id'])).update(is_active = False)
            return HttpResponse(json.dumps({'status': 'Deleted'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'status': 'M3'}))
     
#Distributor Details CRUD Opertaion
class DistributorDetailsCRUD(APIView):
    def get(self, request):
        try:
            # your code...
            print ("---------Company Details Get------",request.body)
            queryset = DistributorDetails.objects.filter(is_active = True).all()
            serializer = DistributorDetailsSerializer(queryset,many=True)
            print "==========ss",serializer.data
            return HttpResponse(json.dumps({'data': serializer.data,'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'}))
        
    def post(self, request):
        try:
            print ("---------Company Details POST------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['name'])
            # your code...
            AddStatus = DistributorDetails(name = str(datas['data'][0]['name']),email = str(datas['data'][0]['email']),mobile = str(datas['data'][0]['mobile']),phone = str(datas['data'][0]['phone']),address1 = str(datas['data'][0]['address1']),address2 = str(datas['data'][0]['address2']),company_id = int(datas['data'][0]['company']))
            AddStatus.save()
            if AddStatus.id:
                return HttpResponse(json.dumps({'status': 'M1'}))
            return HttpResponse(json.dumps({'status': 'M2'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
            
    def put(self, request):
        try:
            # your code...
            print ("---------Company Details Put------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = DistributorDetails.objects.filter(id = int(datas['data'][0]['id'])).update(name = str(datas['data'][0]['name']),email = str(datas['data'][0]['email']),mobile = str(datas['data'][0]['mobile']),phone = str(datas['data'][0]['phone']),address1 = str(datas['data'][0]['address1']),address2 = str(datas['data'][0]['address2']),company_id = int(datas['data'][0]['company']))
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                
    def delete(self, request):
        try:
            # your code...
            print ("---------Compan yDetails Delete------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = DistributorDetails.objects.filter(id = int(datas['data'][0]['id'])).update(is_active = False)
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 

#Route Details CRUD Opertaion
class RouteDetailsCRUD(APIView):
    def get(self, request):
        try:
            # your code...
            print ("---------Route Details Details Get------",request.body)
            queryset = RouteDetails.objects.filter(is_active = True).all()
            serializer = RouteDetailsSerializer(queryset,many=True)
            print "==========ss",serializer.data
            return HttpResponse(json.dumps({'data': serializer.data,'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'}))
        
    def post(self, request):
        try:
            print ("---------Route Details Details POST------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['name'])
            # your code...
            AddStatus = RouteDetails(name = str(datas['data'][0]['name']),address = str(datas['data'][0]['address']))
            AddStatus.save()
            if AddStatus.id:
                return HttpResponse(json.dumps({'status': 'M1'}))
            return HttpResponse(json.dumps({'status': 'M2'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
            
    def put(self, request):
        try:
            # your code...
            print ("---------Route Details Details Put------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = RouteDetails.objects.filter(id = int(datas['data'][0]['id'])).update(name = str(datas['data'][0]['name']),address = str(datas['data'][0]['address']))
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                
    def delete(self, request):
        try:
            # your code...
            print ("---------Route Details Details Delete------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = RouteDetails.objects.filter(id = int(datas['data'][0]['id'])).update(is_active = False)
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                    
#Area Details CRUD Opertaion
class AreaDetailsCRUD(APIView):
    def get(self, request):
        try:
            # your code...
            print ("---------Area Details Details Get------",request.body)
            queryset = AreaDetails.objects.filter(is_active = True).all()
            serializer = AreaDetailsSerializer(queryset,many=True)
            print "==========ss",serializer.data
            return HttpResponse(json.dumps({'data': serializer.data,'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'}))
        
    def post(self, request):
        try:
            print ("---------Area Details Details POST------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['name'])
            # your code...
            AddStatus = AreaDetails(name = str(datas['data'][0]['name']),address = str(datas['data'][0]['address']),pin = str(datas['data'][0]['pin']),distributor_id = int(datas['data'][0]['distributor']),route_id = int(datas['data'][0]['route']))
            AddStatus.save()
            if AddStatus.id:
                return HttpResponse(json.dumps({'status': 'M1'}))
            return HttpResponse(json.dumps({'status': 'M2'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
            
    def put(self, request):
        try:
            # your code...
            print ("---------Area Details Details Put------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = AreaDetails.objects.filter(id = int(datas['data'][0]['id'])).update(name = str(datas['data'][0]['name']),address = str(datas['data'][0]['address']),pin = str(datas['data'][0]['pin']),distributor_id = int(datas['data'][0]['distributor']),route_id = int(datas['data'][0]['route']))
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                
    def delete(self, request):
        try:
            # your code...
            print ("---------Area Details Details Delete------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = AreaDetails.objects.filter(id = int(datas['data'][0]['id'])).update(is_active = False)
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
     
#customer Details CRUD Opertaion
class CustomerDetailsCRUD(APIView):
    def get(self, request):
        try:
            # your code...
            print ("---------Customer Details Details Get------",request.body)
            queryset = CustomerDetails.objects.filter(is_active = True).all()
            serializer = CustomerDetailsSerializer(queryset,many=True)
            print "==========ss",serializer.data
            return HttpResponse(json.dumps({'data': serializer.data,'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'}))
        
    def post(self, request):
        try:
            print ("---------Customer Details Details POST------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['name'])
            # your code...
            AddStatus = CustomerDetails(name = str(datas['data'][0]['name']),email = str(datas['data'][0]['email']),mobile = str(datas['data'][0]['mobile']),phone = str(datas['data'][0]['phone']),address1 = str(datas['data'][0]['address1']),address2 = str(datas['data'][0]['address2']),company_id = int(datas['data'][0]['company']))
            AddStatus.save()
            if AddStatus.id:
                return HttpResponse(json.dumps({'status': 'M1'}))
            return HttpResponse(json.dumps({'status': 'M2'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
            
    def put(self, request):
        try:
            # your code...
            print ("---------Customer Details Details Put------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = CustomerDetails.objects.filter(id = int(datas['data'][0]['id'])).update(name = str(datas['data'][0]['name']),email = str(datas['data'][0]['email']),mobile = str(datas['data'][0]['mobile']),phone = str(datas['data'][0]['phone']),address1 = str(datas['data'][0]['address1']),address2 = str(datas['data'][0]['address2']),company_id = int(datas['data'][0]['company']))
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                
    def delete(self, request):
        try:
            # your code...
            print ("---------Customer Details Details Delete------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = CustomerDetails.objects.filter(id = int(datas['data'][0]['id'])).update(is_active = False)
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                                   
#Project Category Details CRUD Opertaion
class ProductCategoryDetailsCRUD(APIView):
    def get(self, request):
        try:
            # your code...
            print ("---------Project Category Details Details Get------",request.body)
            queryset = ProductCategoryDetails.objects.filter(is_active = True).all()
            serializer = ProductCategoryDetailsSerializer(queryset,many=True)
            print "==========ss",serializer.data
            return HttpResponse(json.dumps({'data': serializer.data,'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'}))
        
    def post(self, request):
        try:
            print ("---------Project Category Details Details POST------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['name'])
            # your code...
            AddStatus = ProductCategoryDetails(name = str(datas['data'][0]['name']))
            AddStatus.save()
            if AddStatus.id:
                return HttpResponse(json.dumps({'status': 'M1'}))
            return HttpResponse(json.dumps({'status': 'M2'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
            
    def put(self, request):
        try:
            # your code...
            print ("---------Project Category Details Details Put------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = ProductCategoryDetails.objects.filter(id = int(datas['data'][0]['id'])).update(name = str(datas['data'][0]['name']))
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                
    def delete(self, request):
        try:
            # your code...
            print ("---------Project Category Details Details Delete------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = ProductCategoryDetails.objects.filter(id = int(datas['data'][0]['id'])).update(is_active = False)
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
    
#Project Details CRUD Opertaion
class ProductDetailsCRUD(APIView):
    def get(self, request):
        try:
            # your code...
            print ("---------Project Details Details Get------",request.body)
            queryset = ProductDetails.objects.filter(is_active = True).all()
            serializer = ProductDetailsSerializer(queryset,many=True)
            print "==========ss",serializer.data
            return HttpResponse(json.dumps({'data': serializer.data,'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'}))
        
    def post(self, request):
        try:
            print ("---------Project Details Details POST------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['name'])
            # your code...
            AddStatus = ProductDetails(name = str(datas['data'][0]['name']),price = float(datas['data'][0]['price']),quantity = int(datas['data'][0]['quantity']),category_id = int(datas['data'][0]['category']),company_id = int(datas['data'][0]['company']))
            AddStatus.save()
            if AddStatus.id:
                return HttpResponse(json.dumps({'status': 'M1'}))
            return HttpResponse(json.dumps({'status': 'M2'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
            
    def put(self, request):
        try:
            # your code...
            print ("---------Project Details Details Put------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = ProductDetails.objects.filter(id = int(datas['data'][0]['id'])).update(name = str(datas['data'][0]['name']),price = float(datas['data'][0]['price']),quantity = int(datas['data'][0]['quantity']),category_id = int(datas['data'][0]['category']),company_id = int(datas['data'][0]['company']))
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                
    def delete(self, request):
        try:
            # your code...
            print ("---------Project Details Details Delete------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = ProductDetails.objects.filter(id = int(datas['data'][0]['id'])).update(is_active = False)
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                    
#Order Details CRUD Opertaion
class OrderDetailsCRUD(APIView):
    def get(self, request):
        try:
            # your code...
            print ("---------Order Details Details Get------",request.body)
            queryset = OrderDetails.objects.filter(is_active = True).all()
            serializer = OrderDetailsSerializer(queryset,many=True)
            print "==========ss",serializer.data
            return HttpResponse(json.dumps({'data': serializer.data,'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'}))
        
    def post(self, request):
        try:
            print ("---------Order Details Details POST------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['quantity'])
            # your code...
            AddStatus = OrderDetails(quantity = int(datas['data'][0]['quantity']),order_date = str(datas['data'][0]['order_date']),from_date = str(datas['data'][0]['from_date']),to_date = str(datas['data'][0]['to_date']),price = float(datas['data'][0]['price']),product_id = int(datas['data'][0]['product']),customer_id = int(datas['data'][0]['customer']),area_id = int(datas['data'][0]['area']),route_id = int(datas['data'][0]['route']),company_id = int(datas['data'][0]['company']))
            AddStatus.save()
            if AddStatus.id:
                return HttpResponse(json.dumps({'status': 'M1'}))
            return HttpResponse(json.dumps({'status': 'M2'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
            
    def put(self, request):
        try:
            # your code...
            print ("---------Order Details Details Put------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = OrderDetails.objects.filter(id = int(datas['data'][0]['id'])).update(quantity = int(datas['data'][0]['quantity']),order_date = str(datas['data'][0]['order_date']),from_date = str(datas['data'][0]['from_date']),to_date = str(datas['data'][0]['to_date']),price = float(datas['data'][0]['price']),product_id = int(datas['data'][0]['product']),customer_id = int(datas['data'][0]['customer']),area_id = int(datas['data'][0]['area']),route_id = int(datas['data'][0]['route']),company_id = int(datas['data'][0]['company']))
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                
    def delete(self, request):
        try:
            # your code...
            print ("---------Order Details Details Delete------",request.body)
            datas = json.loads(request.body);
            print ("-----------===========-----",datas['data'][0]['id'])
            AddStatus = OrderDetails.objects.filter(id = int(datas['data'][0]['id'])).update(is_active = False)
            return HttpResponse(json.dumps({'status': 'M1'}))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps({'data': [],'status':'M3'})) 
                                        
#404 error
def error_404(request):
    return render(request,'404.html', {})
   
#404 error
def error_500(request):
    return render(request,'500.html', {})
    