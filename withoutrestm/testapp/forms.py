from django import forms
from django.forms import fields
from .models import Employee


class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal = self.cleaned_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('The salary should be minimum 5000')
        return inputsal

    class Meta:
        model = Employee
        fields = '__all__'
