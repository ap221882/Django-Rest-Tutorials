from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


from .models import Employee

from testapp.mixins import SerializeMixin
from testapp.mixins import HttpResponseMixin
from .forms import EmployeeForm


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


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        # json_data = json.dumps({'msg': 'you sent valid json data only'})
        # return self.render_to_http_response(json_data, status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created'})
            return self.render_to_http_response(json_data, status=400)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)
