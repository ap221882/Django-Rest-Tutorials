from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from django.core.serializers import serialize

from .models import Employee

import json
# Create your views here.
from testapp.mixins import SerializeMixin


class EmployeeDetailsCBV(SerializeMixin, View):
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        json_data = serialize(
            'json', [emp, ], fields=('eno', 'ename', 'eaddr'))
        return HttpResponse(json_data, content_type='application/json')


class EmployeeListCBV(SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')

# class EmployeeListCBV(SerializeMixin, View):
#     def get(self, request, *args, **kwargs):
#         qs = Employee.objects.all()
#         json_data = serialize(
#             'json', qs)
#         # json_data = serialize(
#         #     'json', qs, fields=('eno', 'ename', 'eaddr'))
#         p_data = json.loads(json_data)
#         print(p_data)
#         final_list = []
#         for obj in p_data:
#             emp_data = obj['fields']
#             final_list.append(emp_data)
#         json_data = json.dumps(final_list)
#         return HttpResponse(json_data, content_type='application/json')


# class EmployeeDetailsCBV(View):
#     def get(self, request, id, *args, **kwargs):
#         emp = Employee.objects.get(id=id)
#         # emp_data = {
#         #     'eno':emp.eno,
#         #     'ename':emp.ename,
#         #     'esal':emp.esal,
#         #     'eaddr':emp.eaddr,
#         # }
#         # json_data = json.dumps(emp_data)
#         json_data = serialize('json', [emp, ])
#         return HttpResponse(json_data, content_type='application/json')

# Model => [Dictionary => JsonData] is called as Serialization
