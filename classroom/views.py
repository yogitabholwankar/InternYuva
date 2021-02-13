from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Course,Faculty
from .forms import CreateCourse,AddVideos,AddNotes
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
	course_videos=course.video_lectures.all()
	course_notes=course.notes.all()
	context={
		'object':course,
		'videos':course_videos,
		'notes':course_notes,
	}
	return render(request,'classroom/course_detail.html',context)

@login_required
def createCourse(request):
	form=CreateCourse()
	slug=""
	current_faculty_user=Faculty.objects.get(user=request.user)
	if current_faculty_user is None:
		messages.warning(request, "Sorry You are not allow to create course")
		return redirect('login')

	if request.method=="POST":
		form=CreateCourse(request.POST or None,request.FILES or None)
		if form.is_valid():
			course=form.save(commit=False)
			course.faculty=current_faculty_user
			course.save()
			slug=course.slug
			# redirect('course_detail',course_.slug)
			return redirect('add_videos_to_course',slug)

	context={
		'form':form,
	}
	return render(request,'classroom/course_create.html',context)

@login_required()
def addVideosToCourse(request,course_slug):
	current_course=Course.objects.get(slug=course_slug)
	current_faculty_user = Faculty.objects.get(user=request.user)
	if current_faculty_user is None:
		messages.warning(request, "Sorry You are not allow to make any changes")
		return redirect('login')

	if current_course.faculty != current_faculty_user:
		messages.warning(request,"Sorry You Can't Make nay changes")
		return redirect('home')

	form = AddVideos()
	if request.method=="POST":
		form=AddVideos(request.POST or None, request.FILES or None)
		if form.is_valid():
			video=form.save(commit=False)
			video.save()
			current_course.video_lectures.add(video)
			current_course.save()
			messages.info(request, "Videos are successfully added to course")
			return redirect('course_detail',course_slug)
	context={
		'form':form,
		'course':current_course,
	}
	return render(request,'classroom/course_add_videos.html',context)

@login_required()
def addNotesToCourse(request,course_slug):
	current_course=Course.objects.get(slug=course_slug)
	current_faculty_user = Faculty.objects.get(user=request.user)
	if current_faculty_user is None:
		messages.warning(request, "Sorry You are not allow to make any changes")
		return redirect('login')

	if current_course.faculty != current_faculty_user:
		messages.warning(request,"Sorry You Can't Make nay changes")
		return redirect('home')

	form = AddNotes()
	if request.method=="POST":
		form=AddNotes(request.POST or None, request.FILES or None)
		if form.is_valid():
			notes=form.save(commit=False)
			notes.save()
			current_course.notes.add(notes)
			current_course.save()
			messages.info(request,"Notes are successfully added to course")
			return redirect('course_detail',course_slug)
	context={
		'form':form,
		'course':current_course,
	}
	return render(request,'classroom/course_add_notes.html',context)




