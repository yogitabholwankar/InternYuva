from django.urls import path
from dprocess import views


urlpatterns = [
	path('', views.home, name='homepage'),
	path('dashboard/', views.dashboard, name='dashboard'),


]