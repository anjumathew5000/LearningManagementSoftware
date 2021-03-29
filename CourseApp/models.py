from django.db import models

# Create your models here.
class Courses(models.Model):
    Course_name=models.CharField(max_length=150,null=True,blank=True)
    Course_description=models.TextField(null=True,blank=True)
    Course_stream=models.CharField(max_length=30,null=True,blank=True)
    Couser_Image=models.ImageField(upload_to="courseImage",null=True,blank=True)