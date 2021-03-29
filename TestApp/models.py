from django.db import models
from CourseApp.models import Courses

# Create your models here.
class Tests(models.Model):
    Course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True,blank=True)
    test_id=models.CharField(max_length=30,null=True,blank=True)
    test_duration=models.IntegerField(null=True,blank=True)
    test_totalmark=models.IntegerField(null=True,blank=True)

