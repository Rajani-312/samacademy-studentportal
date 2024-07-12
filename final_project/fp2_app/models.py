from django.shortcuts import render
from django.db import models

# Create your models here.
class project2(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)

class Meta:
    db_table="project2"