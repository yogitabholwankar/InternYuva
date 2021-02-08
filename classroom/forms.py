from django import forms
from .models import Course



class CreateCourse(forms.ModelForm):
    class Meta:
        model=Course
        fields=['name','sub_category','price','thumbnail','is_active','is_completed','is_live']