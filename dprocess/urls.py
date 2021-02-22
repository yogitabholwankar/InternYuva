from django.urls import path
from dprocess import views


urlpatterns = [
	path('', views.home, name='homepage'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('dashboard/profile/', views.profile, name='profile'),
	path('course_purchage/', views.course_purchage, name='course_purchage'),
	path('dashboard/checkout/', views.checkout, name='checkout'),
	path('dashboard/handlerequest/', views.handlerequest, name='handlerequest'),


]