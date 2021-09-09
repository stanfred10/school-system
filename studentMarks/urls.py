from django.urls import path
from . import views

urlpatterns = [
	# /studentMarks/
	path('', views.index, name="marks"),

	path('detail/<str:pk>/', views.detail, name="detail"),
	path('detail', views.time, name="detail"),
	path('delete/<str:pk>/', views.deleteStudent, name="delete"),
]