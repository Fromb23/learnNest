from django.db import models
class Subject(models.Model):
    name = models.CharField(max_length=150)

class Student(models.Model):
    student_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject, related_name='students')
    password = models.CharField(max_length=100)

class Tutor(models.Model):
    tsc_no = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subj_comb = models.ManyToManyField(Subject, related_name='tutors')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
