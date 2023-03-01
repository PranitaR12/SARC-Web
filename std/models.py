from django.db import models

# Create your models here.
class Student(models.Model):
    event=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=150)
    description=models.CharField(max_length=200)
    contact=models.CharField(max_length=10)