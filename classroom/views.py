from django.shortcuts import render
from .models import *

def room(request):
	pass


def course_purchage(request):
	rating = Ratings.objects.all().count() 
	return render(request, 'course/course_purchage.html', {'rating':rating})	