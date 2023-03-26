from django.shortcuts import render
from  app.models import dados
from app.serializers import dadosSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

class dadosViewSet(viewsets.ModelViewSet):
    queryset = dados.objects.all()
    serializer_class = dadosSerializer


