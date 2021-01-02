from django import forms
from .models import Courses
from django.core import validators

class CoursesDetails(forms.ModelForm):
    class Meta:
        model= Courses
        fields= ("course_name","course_provider_name","img_of_course","img_of_provider","category","start_date","end_date")
        widgets = {
        "course_name" : forms.TextInput(attrs = {"class" : "form-control"}),
        "course_provider_name":forms.TextInput(attrs = {"class" : "form-control"}),
        "img_of_course" : forms.FileInput(attrs = {"class" : "form-control"}),
        "img_of_provider" : forms.FileInput(attrs = {"class" : "form-control"}),
        "category" : forms.TextInput(attrs = {"class" : "form-control"}),
        "start_date" : forms.DateInput(attrs = {"class" : "form-control"}),
        "end_date" : forms.DateInput(attrs = {"class" : "form-control"}),
        }
