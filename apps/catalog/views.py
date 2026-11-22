from django.shortcuts import render

from apps.catalog.models import Flower, FlowerGrade, FlowerVariety
from .serializers import FlowerSerializer, FlowerGradeSerializer, FlowerVarietySerializer
from rest_framework import viewsets
# Create your views here.

class FlowerViewSet(viewsets.ModelViewSet):
    serializer_class = FlowerSerializer
    queryset = Flower.objects.all()

class FlowerVarietyViewSet(viewsets.ModelViewSet):
    serializer_class = FlowerVarietySerializer
    queryset = FlowerVariety.objects.all()

class FlowerGradeViewSet(viewsets.ModelViewSet):
    serializer_class = FlowerGradeSerializer
    queryset = FlowerGrade.objects.all()
