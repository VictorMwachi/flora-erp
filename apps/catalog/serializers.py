from rest_framework import serializers
from .models import Flower, FlowerGrade

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'

class FlowerGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerGrade
        fields = '__all__'