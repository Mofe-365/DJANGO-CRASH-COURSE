from django.db import models
from django.db.models import aggregates
from django.shortcuts import render
from django.db import models

class Todo(models.Model):
    Name = models.CharField(max_length=100)
    Due_Date = models.DateField()

    def __str__(self):
        return self.Name

class personal_info(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    age = models.IntegerField(default=15)
    job = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.First_Name} {self.Last_Name}'