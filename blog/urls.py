from django.urls import path
from blog import views


urlpatterns = [
	path('', views.blog_home,name='blog_home'),
]

# TODO

