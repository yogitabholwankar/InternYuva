from django.contrib import admin
from .models import (CourseGroup, Course, Faculty, Student,
                     Category, SubCategory, Notes,Video_Lecture,
                     Ratings, CourseOverview,VideoTesting,FrequentlyAskQuestion
                     )

# Register your models here.
admin.site.register(CourseGroup)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Notes)
admin.site.register(SubCategory)
admin.site.register(Ratings)

admin.site.register(CourseOverview)

admin.site.register(VideoTesting)
admin.site.register(Video_Lecture)


admin.site.register(FrequentlyAskQuestion)

