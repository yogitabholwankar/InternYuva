from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import CreateCourse, AddVideos, AddNotes, AddCourseOverview
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import NewslettersSubscribers
def room(request):
	pass



def index(request):
	context = {
		'categories':Category.objects.all(),
		'courses': Course.objects.all(),
		'frequently_ask_questions':FrequentlyAskQuestion.objects.all(),
		'latest_course':Course.objects.all().order_by('date_of_created')
	}

	if request.method=="POST":
		email=request.POST.get('news_email')
		user=NewslettersSubscribers.objects.create(email=email)
		return redirect('home')

	return render(request,'main/index.html',context)







def courseListView(request):
	context={
		'objects':Course.objects.all()
		}
	return render(request,'classroom/course_list.html',context)


def courseDetailView(request,slug):
	course=Course.objects.get(slug=slug)

	related_cat=course.category
	related_courses=Course.objects.filter(category=related_cat)
	demo_video=course.video_lectures.get(index=0)

	context={
		'related_courses':related_courses,
		'course':course,
		'videos':course.video_lectures.all(),
		'notes':course.notes.all(),
		'demo_video':demo_video.video_url,
	}
	print(demo_video,222222222)
	return render(request,'main/course-details.html',context)



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

@login_required()
def addCourseOverviewToCourse(request,course_slug):
	current_course=Course.objects.get(slug=course_slug)
	current_faculty_user = Faculty.objects.get(user=request.user)
	if current_faculty_user is None:
		messages.warning(request, "Sorry You are not allow to make any changes")
		return redirect('login')

	if current_course.faculty != current_faculty_user:
		messages.warning(request,"Sorry You Can't Make nay changes")
		return redirect('home')

	form = AddCourseOverview()
	if request.method=="POST":
		form=AddCourseOverview(request.POST or None, request.FILES or None)
		if form.is_valid():
			lines=form.save(commit=False)
			lines.save()
			current_course.course_overview.add(lines)
			current_course.save()
			messages.info(request,"Course Overview are successfully added to course")
			return redirect('course_detail',course_slug)
	context={
		'form':form,
		'course':current_course,
	}
	return render(request,'classroom/course_add_course_overview.html',context)


def videoTesting(request):
	videos=VideoTesting.objects.all()
	context={
		'videos':videos
	}
	return render(request,'classroom/vidTesting.html',context)




def contactUs(request):
	if request.method=="POST":
		name=request.POST.get('name')
		email=request.POST.get('email')
		phone_number=request.POST.get('phone_number')
		message=request.POST.get('message')
		print([name,email,phone_number,message])
		curr_form=ContactForm.objects.create(name=name,email=email,phone_number=phone_number,message=message)
		curr_form.save()

		"""Add redirect message"""
		return redirect('contact_us')
	return render(request,'main/contact.html')

def aboutUs(request):
	return render(request,'main/about.html')
