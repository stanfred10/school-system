from django import forms
from django.forms import ModelForm

from .models import *


class StudentForm(forms.ModelForm):
	student_name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new student...'}))
	course_name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new course...'}))
	age= forms.IntegerField(widget= forms.TextInput(attrs={'placeholder':'Add Age...'}))

	class Meta:
		model = Student
		fields = '__all__' 