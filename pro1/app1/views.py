from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from . serializers import EmployeeSerializer
from . models import Employee
# Create your views here.

class EmployeeApi(CreateAPIView,ListAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

class EmployeeDetials(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()