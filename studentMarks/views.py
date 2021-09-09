from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

from .models import Student
from .forms import *

# Create your views here.

def index(request):
	all_students = Student.objects.all()

	form = StudentForm()

	if request.method =='POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')	

	context = {'all_students':all_students, 'form':form}
	return render(request, 'studentMarks/marks.html', context)
		

def detail(request, pk):
	try:
		student = Student.objects.get(id=pk)
	except Student.doesNotExist:
		raise Http404("Student does not exist")
	return render(request, 'studentMarks/detail.html', {'student': student})

def deleteStudent(request, pk):
	item = Student.objects.get(pk=pk)

	if request.method == 'POST':		
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'studentMarks/delete.html', context)

def time(request):
	return render(request, 'studentMarks/detail.html')
