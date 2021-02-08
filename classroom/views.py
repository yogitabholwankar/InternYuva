from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Course,Faculty
from .forms import CreateCourse
from django.contrib.auth.decorators import login_required
# Create your views here.


def room(request):
	pass


def courseListView(request):
	context={
		'objects':Course.objects.all()
	}
	return render(request,'classroom/course_list.html',context)


def courseDetailView(request,slug):
	course=Course.objects.get(slug=slug)
	context={
		'object':course
	}
	return render(request,'classroom/course_detail.html',context)

@login_required
def createCourse(request):
	form=CreateCourse()
	current_faculty_user=Faculty.objects.get(user=request.user)
	if current_faculty_user is None:
		messages.warning(request, "Sorry You are not allow to create course")
		return redirect('home')

	if request.method=="POST":
		form=CreateCourse(request.POST or None,request.FILES or None)
		if form.is_valid():
			form.save(commit=False)
			form.faculty=current_faculty_user
			form.save()
			course_=form
			# redirect('course_detail',course_.slug)
			return redirect('course_list')

	context={
		'form':form,
	}
	return render(request,'classroom/course_create.html',context)