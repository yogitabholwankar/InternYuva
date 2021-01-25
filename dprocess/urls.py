from django.urls import path
from dprocess import views


urlpatterns = [
	path('', views.home, name='homepage'),
]