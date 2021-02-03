from django.db import models
class CourseModel(models.Model):
    Name=models.CharField(max_length=30,unique=True)
    faculty=models.CharField(max_length=30)
    Date=models.DateField(auto_now_add=True)
    Time=models.TimeField()
    fee=models.FloatField()
    duration=models.IntegerField()
class StudentModel(models.Model):
    name=models.CharField(max_length=30)
    contactno=models.IntegerField(unique=True)
    Email=models.CharField(unique=True,max_length=30)
    Password=models.CharField(max_length=30)