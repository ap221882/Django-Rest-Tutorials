from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json
def emp_data_jsonview(request):
    emp_data = {
        'emp':100,
        'ename':'Ajay',
        'empsal':1000,
        'empaddr':'Mumbai',
    }
    return JsonResponse(emp_data)
    # json_data = json.dumps(emp_data)
    # return HttpResponse(json_data,content_type='application/json')