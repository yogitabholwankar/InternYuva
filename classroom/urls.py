from django.urls import path
from classroom import views


urlpatterns = [
	path('', views.index, name='home'),
	path('course_list/',views.courseListView,name='course_list'),
	path('course/<slug>',views.courseDetailView ,name='course_detail'),


	#ToDO Course Creation
	path('course/add_videos/<course_slug>',views.addVideosToCourse ,name='add_videos_to_course'),
	path('course/add_notes/<course_slug>',views.addNotesToCourse ,name='add_notes_to_course'),
	path('create_course/',views.createCourse,name='create_course'),

	path('vid/',views.videoTesting),

	#Static Pages
	path('contact_us/',views.contactUs,name="contact_us"),
	path('about_us/',views.aboutUs,name="about_us"),

	path('internships/',views.internships,name='internships'),
	path('internships/<id>',views.internshipDetail,name='internships-detail'),

	#checkout page
	path('checkout/<course_slug>',views.checkoutPage,name="checkout"),

	#user course
	path('purchase_course/',views.user_courseListView,name='purchase_course'),

	#course-detail-view-for-member
	path('course/<course_slug>/video',views.course_detail_view_for_purchase_user,name='course-access')



]


"""
====== Server Task ======

1. Payment
2. S3 Bucket 
3. Google Auth
4. host on aws

====== Backend Task =======

1. redirection
2. courses list page categories
3. email auth/otp
4. favourites
5. profile edit page
6. password change fields
7. in classroom/notes model add proper path and file name in media folder , check save() method


====== Frontend Task =======

1. Blog Detail Page   
2. Profile Page  
3. Content
4. Active Button On Navbar Home
5. Mobile View Profile DropDown
6. Course Access Page Separated Notes And Videos
7. reduce margin of course list

"""

#todo
# python manage.py loaddata db.json
# if you added some data or change anything in models.py
# python manage.py dumpdata > db.json

