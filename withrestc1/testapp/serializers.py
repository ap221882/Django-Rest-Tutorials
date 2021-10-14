import re
from django.db.models import fields
from rest_framework import serializers


from .models import Employee


def multiples_of_1000(value):
    if value % 1000 != 0:
        raise serializers.ValidationError(
            'Employee salary should be in multiple of 1000s')


class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiples_of_1000])

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['eno','enum']
        # exclude = ['esal']


# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=64)
#     esal = serializers.FloatField(validators=[multiples_of_1000])
#     eaddr = serializers.CharField(max_length=64)

#     def validate(self, data):
#         ename = data.get('ename')
#         esal = data.get('esal')
#         if ename.lower() == 'sunny':
#             if esal < 50000:
#                 raise serializers.ValidationError(
#                     'Sunny salry should be minimum 50000')
#         return data

#     def validate_esal(self, value):
#         if value < 5000:
#             raise serializers.ValidationError(
#                 'Employee salary must be minimum 5000')
#         return value

#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.eno = validated_data.get('eno', instance.eno)
#         instance.ename = validated_data.get('ename', instance.ename)
#         instance.esal = validated_data.get('esal', instance.esal)
#         instance.eaddr = validated_data.get('eaddr', instance.eaddr)
#         instance.save()
#         return instance
