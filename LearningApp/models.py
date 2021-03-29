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














    



