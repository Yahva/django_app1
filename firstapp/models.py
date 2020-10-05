from django.db import models

# Create your models here.
class Patient(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    age = models.IntegerField()