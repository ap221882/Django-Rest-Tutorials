from typing import OrderedDict
from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']


admin.site.register(Employee, EmployeeAdmin)