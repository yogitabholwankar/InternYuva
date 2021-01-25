from django.urls import path
from classroom import views


urlpatterns = [
	path('classroom/', views.room, name='room'),
]