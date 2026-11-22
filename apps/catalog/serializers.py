from rest_framework import serializers
from .models import Flower, FlowerGrade, FlowerVariety

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'

class FlowerVarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerVariety
        fields = '__all__'

class FlowerGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerGrade
        fields = '__all__'