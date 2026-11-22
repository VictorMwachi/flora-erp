from django.db import models

# Create your models here.
class Flower(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    botanical_name = models.CharField(max_length=100, null=True, blank=True)
    availability = models.CharField(max_length=100,default = "Year Round", null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    market_specifications = models.TextField(null=True, blank=True)
    head_size_specifications = models.CharField(max_length=100, null=True, blank=True)
    pack_rate_stems = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    #image = models.ImageField(upload_to='flowers/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class FlowerVariety(models.Model):
    id = models.AutoField(primary_key=True)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    variety_code = models.CharField(max_length=10, unique=True)
    variety_name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.variety_name} ({self.variety_code})"

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