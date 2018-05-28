from django.contrib.auth.models import User
from django.shortcuts import render
#logout function here
from django.contrib.auth import authenticate, login,logout 
#template render html
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#custom test models refer
from django.http import HttpResponse,HttpResponseRedirect
import json

#login render page
def loginPage(request):
    return render(request,'./login.html', {})

#sites render page
def sitePage(request):
    try:
        print("---------- User----------",request.user)
        if request.user.is_authenticated():
                return render(request,'./index.html', {"user_name":request.user,"user_id":request.user.id})
        else:
            return HttpResponseRedirect("/")
    except Exception  as e:
        print e
        return HttpResponseRedirect("/")
   
#logout function here
def logoutPage(request):
    try:
        logout(request)
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/")
    except:
        return HttpResponseRedirect("/")
   
