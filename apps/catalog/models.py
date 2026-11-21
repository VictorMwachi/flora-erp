from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    market_specifications = models.TextField()
    head_size = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='flowers/')

class FlowerGrade(models.model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)