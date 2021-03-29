from django.db import models

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








#course and Test module
class Courses(models.Model):
    Course_name=models.CharField(max_length=30,null=True,blank=True)
    Course_description=models.TextField(null=True,blank=True)
    Couser_stream=models.CharField(max_length=30,null=True,blank=True)
class Tests(models.Model):
    Course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True,blank=True)
    test_id=models.CharField(max_length=30,null=True,blank=True)
    test_duration=models.IntegerField(null=True,blank=True)
    test_totalmark=models.IntegerField(null=True,blank=True)



    



