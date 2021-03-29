from django.db import models
from CourseApp.models import Courses

# Create your models here.

#Student Module
class Students(models.Model):
    Student_name=models.CharField(max_length=30,null=True,blank=True)
    Student_email=models.EmailField(max_length=30,null=True,blank=True)
    Student_username=models.CharField(max_length=30,null=True,blank=True)
    Student_password=models.CharField(max_length=30,null=True,blank=True)
    Student_address=models.TextField(null=True,blank=True)
    date_of_reg=models.DateField()
    Course_stream=models.CharField(max_length=50,null=True,blank=True)
    
class Student_course_enrolment(models.Model):
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    date_entrollment=models.DateField()
    date_of_completion=models.DateField(null=True,blank=True)
    

class Student_course_Wishlist(models.Model):
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)


















    



