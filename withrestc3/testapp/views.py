import re
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response

from rest_framework import mixins


class EmployeeListModelMixin(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeRetrieveUpdateDestroyModelMixin(mixins.DestroyModelMixin, generics.RetrieveAPIView, mixins.UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
