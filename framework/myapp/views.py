from django.shortcuts import render,HttpResponse,redirect
from rest_framework import viewsets
from .models import *
from django.contrib.auth  import login, logout,authenticate

# Create your views here.
class employeeDetails(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeeserializer
    search_fields = ['Name','phone_number','address']

def loggin(request):
    return render(request,'login.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user != None:
            login(request,user)
        return redirect(staff_details)
    return redirect(loggin)
def staff_details(request):
    objs = employees.objects.all()
    d= {
        'records': objs
    }
    return render(request,'details.html',d)