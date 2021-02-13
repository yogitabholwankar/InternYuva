from django.contrib import admin
from .models import CourseGroup,Course,Faculty,Student,Category,SubCategory,Note,Ratings
# Register your models here.
admin.site.register(CourseGroup)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Note)
admin.site.register(SubCategory)
admin.site.register(Ratings)
