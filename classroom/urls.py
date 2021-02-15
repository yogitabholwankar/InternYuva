from django.urls import path
from classroom import views


urlpatterns = [
	path('classroom/', views.room, name='room'),
	path('course_purchage/', views.course_purchage, name='course_purchage'),

	path('courses/',views.courseListView,name='course_list'),
	path('course/<slug>',views.courseDetailView ,name='course_detail'),
	path('course/add_videos/<course_slug>',views.addVideosToCourse ,name='add_videos_to_course'),
	path('course/add_notes/<course_slug>',views.addNotesToCourse ,name='add_notes_to_course'),
	path('create_course/',views.createCourse,name='create_course'),
]

# TODO
"""
1. search
2. add video's
3. add notes
	"""
