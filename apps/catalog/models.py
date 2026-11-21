from django.db import models

# Create your models here.
class Flower(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    flower_type = models.CharField(max_length=100)
    market_specifications = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='flowers/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FlowerGrade(models.Model):
    id = models.AutoField(primary_key=True)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    grade_code = models.CharField(max_length=10, unique=True)
    grade_name = models.CharField(max_length=10)
    stem_length_cm = models.IntegerField()
    head_size_cm = models.IntegerField()
    grade_description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)