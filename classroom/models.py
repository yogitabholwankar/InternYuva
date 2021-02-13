import string

from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from dprocess.models import ModelBase
from .choices import *
import random



from django.conf import settings

User=settings.AUTH_USER_MODEL


class Faculty(models.Model):
	# faculty_name = models.CharField(max_length=255)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user.username)


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	active_status = models.CharField(max_length=255)

	def __str__(self):
		return str(self.user.username)


class Category(models.Model):
	category_name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.category_name)


class SubCategory(models.Model):
	category_name = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
	sub_category_name = models.CharField(max_length=255)

	def __str__(self):
		return str(self.sub_category_name)


class Notes(models.Model):
	name=models.CharField(help_text="Name OF PDF File",blank=True,null=True,max_length=20)
	document = models.FileField(upload_to='documents/')

	def __str__(self):
		return str(self.document)


class Video_Lecture(models.Model):
	name=models.CharField(help_text="Add Name OF Video",blank=True,null=True,max_length=20)
	video = models.FileField(upload_to='documents/')

	def __str__(self):
		return str(self.video)


def generate_random_string():
	length = 6
	while True:
		code = ''.join(random.choices(string.ascii_uppercase, k=length))
		if Course.objects.filter(code=code).count() == 0:
			break
	return code


class Course(models.Model):
	name           = models.CharField(max_length=255)
	category       = models.ForeignKey(Category,    on_delete=models.CASCADE,blank=True,null=True)
	sub_category   = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True,null=True)
	faculty        = models.ForeignKey(Faculty,     on_delete=models.CASCADE,blank=True,null=True)
	students       = models.ManyToManyField(Student,blank=True)
	price          = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
	discount_price = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
	notes          = models.ManyToManyField(Notes, blank=True)
	code           = models.CharField(max_length=20, default=generate_random_string)
	video_lectures = models.ManyToManyField(Video_Lecture,blank=True)
	thumbnail      = models.ImageField(blank=True, null=True)
	slug           = models.SlugField(max_length=250, unique=True)
	is_active      = models.BooleanField(default=True)
	is_completed   = models.BooleanField(default=True)
	is_live        = models.BooleanField(default=False)

	def __str__(self):
		return str(self.name)

	def save(self, *args, **kwargs):
		if not self.id:
			super(Course, self).save(*args, **kwargs)
			string_ = ''.join(random.choices(string.ascii_lowercase, k=6))
			num_ = random.randint(1000, 9999)

			self.slug = slugify(self.name) + "-" + str(string_) + "-" + str(num_)
			super(Course, self).save(*args, **kwargs)

	def get_course_absolute_url(self):
		return reverse('course_detail',kwargs={'slug':self.slug})


class CourseGroup(models.Model):
	course_name = models.CharField(max_length=20, blank=True, null=True)
	students = models.ManyToManyField(Student)
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.course_name)


