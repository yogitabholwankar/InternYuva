from django.urls import path
from classroom import views


urlpatterns = [
	path('classroom/', views.room, name='room'),
	path('course_purchage/', views.course_purchage, name='course_purchage'),
	path('courses/',views.courseListView,name='course_list'),
	path('course/<slug>',views.courseDetailView ,name='course_detail'),
	path('create_course/',views.createCourse,name='create_course'),
]

