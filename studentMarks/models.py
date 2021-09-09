from django.db import models
from django.db import *

# Create your models here.

class Student(models.Model):
	student_ID = models.CharField(max_length=100)
	student_name = models.CharField(max_length=200)
	# address = models.CharField(max_length=200)
	course_name = models.CharField(max_length=200)
	age = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.student_name+ ' - ' + self.student_ID


class Subject(models.Model): 
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject_name = models.CharField(max_length=200)
	mark = models.CharField(max_length=10)


	def __str__(self):
		return self.subject_name
	
