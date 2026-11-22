from django.shortcuts import render

from apps.catalog.models import Flower, FlowerGrade
from .serializers import FlowerSerializer, FlowerGradeSerializer
from rest_framework import viewsets
# Create your views here.

class FlowerViewSet(viewsets.ModelViewSet):
    serializer_class = FlowerSerializer
    queryset = Flower.objects.all()

class FlowerGradeViewSet(viewsets.ModelViewSet):
    serializer_class = FlowerGradeSerializer
    queryset = FlowerGrade.objects.all()
