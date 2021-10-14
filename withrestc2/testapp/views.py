from rest_framework.viewsets import ViewSet
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .serializers import NameSerializer


class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['RED', 'BLUE', 'GREEN']
        return Response({'msg': 'Happy Navratri', 'colors': colors})

    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {}, Happy Navratri!'.format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        return Response({'msg': 'This response is from put method'})

    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'This response is from patch method'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'This response is from delete method'})


class TestViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        colors = ['RED', 'BLUE', 'GREEN']
        return Response({'msg': 'Happy Navratri', 'colors': colors})

    def create(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {}, Happy Navratri!'.format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        return Response({'msg': 'This response is from retrieve method of ViewSet'})

    def update(self, request, pk=None):
        return Response({'msg': 'This response is from update method of ViewSet'})

    def partial_update(self, request, pk=None):
        return Response({'msg': 'This response is from partial_update method of ViewSet'})

    def destroy(self, request, pk=None):
        return Response({'msg': 'This response is from destroy method of ViewSet'})
