from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    class_teacher=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    