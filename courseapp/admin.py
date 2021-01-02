from django.contrib import admin
from .models import Courses
# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
    list_display= ["id",'course_name', 'course_provider_name', 'img_of_course', 'img_of_provider', "category", "start_date", "end_date"]

admin.site.register(Courses,CoursesAdmin)
