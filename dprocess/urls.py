from django.urls import path
from dprocess import views


urlpatterns = [
	path('', views.home, name='homepage'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('dashboard/profile/', views.profile, name='profile'),
	path('dashboard/checkout/', views.checkout, name='checkout'),
	path('dashboard/handlerequest/', views.handlerequest, name='handlerequest'),


]