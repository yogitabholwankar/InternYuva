from django.urls import path
from classroom import views


urlpatterns = [
	path('classroom/', views.room, name='room'),
	path('course_purchage/', views.course_purchage, name='course_purchage'),
]