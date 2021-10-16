from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions

from .models import Employee
from .serializers import EmployeeSerializer

# Custom permissions
from .permissions import IsReadOnly, SunnyPermission

# JWT
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    # permission_classes = [AllowAny, ]
