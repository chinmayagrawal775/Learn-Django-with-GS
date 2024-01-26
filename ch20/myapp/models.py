from django.db import models

# Create your models here.

# Abstract Base Class Inheritance
class CommonFeilds(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        abstract = True


class Student(CommonFeilds):
    fees = models.IntegerField()

class Teacher(CommonFeilds):
    salary = models.IntegerField()


# Multi-Table Inheritance
class ExamCenter(models.Model):
    cname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Examinee(ExamCenter):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()

# Proxy Class
class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True