import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


from .models import Employee

from testapp.mixins import SerializeMixin
from testapp.mixins import HttpResponseMixin


class EmployeeDetailsCBV(SerializeMixin, HttpResponseMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps(
                {'msg': 'The requested resource not available.'})
            return self.render_to_http_response(json_data, status=404)
        else:
            json_data = self.serialize([emp, ])
            return self.render_to_http_response(json_data)


class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)
