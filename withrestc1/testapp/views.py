from functools import partial
import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework import serializers

from .models import Employee

from .serializers import EmployeeSerializer

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_emp = JSONRenderer().render(serializer.data)
            return HttpResponse(json_emp, content_type='application/json', status=200)
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=p_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource created successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=pdata, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg': 'Resource deleted successfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')
