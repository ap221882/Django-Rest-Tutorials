from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.
from rest_framework import generics

from .pagination import MyPagination, MyPagination2, MyPagination3

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination3
