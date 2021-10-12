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


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(SerializeMixin, HttpResponseMixin, View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        python_dict_data = json.loads(data)
        id = python_dict_data.get('id', None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps(
                    {'msg': 'The requested resource not available with matched id.'})
                return self.render_to_http_response(json_data, status=404)
            json_data = self.serialize([emp, ])
            return self.render_to_http_response(json_data)
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

    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        python_dict_data = json.loads(data)
        id = python_dict_data.get('id', None)
        if id is None:
            json_data = json.dumps(
                {'msg': 'to perform updation id is mandtory, please provide id.'})
            return self.render_to_http_response(json_data, status=400)
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps(
                {'msg': 'No matched record found, not possible to perform updation.'})
            return self.render_to_http_response(json_data, status=404)
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        python_dict_data = json.loads(data)
        id = python_dict_data.get('id', None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps(
                    {'msg': 'The requested resource not available with matched id.'})
                return self.render_to_http_response(json_data, status=404)
            status, deleted_item = emp.delete()
            if status == 1:
                json_data = json.dumps(
                    {'msg': 'Resource deleted successfully'})
                return self.render_to_http_response(json_data)
            json_data = json.dumps(
                {'msg': 'Unable to delete, please try again...'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps(
            {'msg': 'to perform updation id is mandtory, please provide id.'})
        return self.render_to_http_response(json_data, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailsCBV(SerializeMixin, HttpResponseMixin, View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

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

    def put(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps(
                {'msg': 'No matched record found, not possible to perform updation.'})
            return self.render_to_http_response(json_data, status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        provided_data = json.loads(data)
        original_data = {
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eaddr': emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps(
                {'msg': 'No matched record found, not possible to perform deletion.'})
            return self.render_to_http_response(json_data, status=404)
        status, deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'Resource deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps(
            {'msg': 'Unable to delete, please try again...'})
        return self.render_to_http_response(json_data)


# @method_decorator(csrf_exempt, name='dispatch')
# class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):
#     def get(self, request, *args, **kwargs):
        # qs = Employee.objects.all()
        # json_data = self.serialize(qs)
        # return self.render_to_http_response(json_data)

    # def post(self, request, *args, **kwargs):
    #     data = request.body
    #     valid_json = is_json(data)
    #     if not valid_json:
    #         json_data = json.dumps({'msg': 'please send valid json data only'})
    #         return self.render_to_http_response(json_data, status=400)
    #     # json_data = json.dumps({'msg': 'you sent valid json data only'})
    #     # return self.render_to_http_response(json_data, status=400)
    #     empdata = json.loads(data)
    #     form = EmployeeForm(empdata)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         json_data = json.dumps({'msg': 'Resource created'})
    #         return self.render_to_http_response(json_data, status=400)
    #     if form.errors:
    #         json_data = json.dumps(form.errors)
    #         return self.render_to_http_response(json_data, status=400)
