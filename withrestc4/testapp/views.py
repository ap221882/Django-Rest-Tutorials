from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions

from .models import Employee
from .serializers import EmployeeSerializer

# Custom permissions
from .permissions import IsReadOnly, SunnyPermission


class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsReadOnly, SunnyPermission]
    # permission_classes = [AllowAny, ]
