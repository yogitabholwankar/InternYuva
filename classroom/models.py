from django.db import models
# from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from dprocess.models import ModelBase
from .choices import *



from django.conf import settings

User=settings.AUTH_USER_MODEL


class Faculty(ModelBase):
	faculty_name = models.CharField(max_length=255)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.faculty_name)


class Student(ModelBase):
	student_name = models.CharField(max_length=255)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	active_status = models.CharField(max_length=255)

	def __str__(self):
		return str(self.student_name)


class Category(ModelBase):
	category_name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.category_name)



class SubCategory(ModelBase):
	sub_category_name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.sub_category_name)


class Note(ModelBase):
	document = models.FileField(upload_to='documents/')

	def __str__(self):
		return str(self.document)


class Video_Lecture(ModelBase):
	video = models.FileField(upload_to='documents/')

	def __str__(self):
		return str(self.video)


class Course(ModelBase):
	name = models.CharField(max_length=255)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	students = models.ManyToManyField(Student, related_name='studentname')
	price = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
	discount_price = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
	notes = models.ManyToManyField(Note)
	code = models.TextField()
	video_lectures = models.ManyToManyField(Video_Lecture)
	thumnails = models.ImageField()
	slug = models.SlugField(max_length=250, unique=True)

	def __str__(self):
		return str(self.name)
		
	def save(self, *args, **kwargs):
		if not self.id:
			super(Course, self).save(*args, **kwargs)
			self.slug = slugify(self.name) + "-" + str(self.user.id) + "-" + str(self.id)
			super(Course, self).save(*args, **kwargs)



class CourseGroup(ModelBase):
	students = models.ManyToManyField(Student)
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.students)


