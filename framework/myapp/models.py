from dataclasses import fields
from encodings import search_function
from pyexpat import model
from django.db import models
from rest_framework import serializers

# Create your models here.
class employees(models.Model):
   Name = models.CharField('Name',max_length=30)
   Date_of_birth = models.DateField('date_of_birth') 
   gender = models.CharField('gender',max_length=6)
   phone_number = models.IntegerField('phone_number')
   address = models.TextField('address')
    
class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'
