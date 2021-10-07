from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


from .models import Employee

from testapp.mixins import SerializeMixin


class EmployeeDetailsCBV(SerializeMixin, View):
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        json_data = self.serialize([emp, ])
        return HttpResponse(json_data, content_type='application/json')


class EmployeeListCBV(SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')
