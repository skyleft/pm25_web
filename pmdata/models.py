from django.db import models

# Create your models here.

#place model
class Place(models.Model):
    city = models.CharField(max_length=10)
    place = models.CharField(max_length=30)

#grade model
class Grade(models.Model):
    grade = models.CharField(max_length=10)

#pollution model
class Pollution(models.Model):
    pollution = models.CharField(max_length=20)

#main data model
class Data(models.Model):
    sid = models.ForeignKey(Place)
    AQI = models.IntegerField()
    grade = models.ForeignKey(Grade)
    pollution = models.ForeignKey(Pollution)
    pm25 = models.IntegerField()
    pm10 = models.IntegerField()
    CO = models.FloatField()
    NO2 = models.IntegerField()
    O31 = models.IntegerField()
    O38 = models.IntegerField()
    SO2 = models.IntegerField()
    date = models.BigIntegerField()