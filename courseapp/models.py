from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    course_provider_name = models.CharField(max_length=255)
    img_of_course = models.ImageField(null=True,blank=True)
    img_of_provider = models.ImageField(null=True,blank=True)
    category = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
