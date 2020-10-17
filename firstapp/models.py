from django.db import models

# Create your models here.
class Patient(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.IntegerField()

class Doctor(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.IntegerField()
    specDoctor = models.IntegerField()

class SpecDoctor(models.Model):
    name = models.CharField(max_length=50)

class Ticket(models.Model):
    time = models.TimeField()
    isBusy = models.BooleanField()
    docID = models.IntegerField()
    patID = models.IntegerField()
    
    
