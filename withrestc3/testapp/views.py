import re
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
# Create your views here.

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# class EmployeeListAPIView(APIView):
#     def get(self, request, format=None):
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs, many=True)  # model to dict
#         return Response(serializer.data)  # dict to json


class EmployeeListAPIView(ListAPIView):
    # queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get('diyahuanaam')
        if name is not None:
            qs = qs.filter(ename__icontains=name)
        return qs


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'  # default is pk


class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
