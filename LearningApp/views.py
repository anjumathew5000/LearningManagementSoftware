from django.shortcuts import render
import datetime
from LearningApp.models import Students
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def Student_register(request):
    if request.method=='POST':
        S_name=request.POST.get('name')
        S_email=request.POST.get('username')
        S_username=request.POST.get('email')
        S_password=request.POST.get('password')
        S_address=request.POST.get('course')
        S_course=request.POST.get('address')
        regdate=datetime.datetime.today()
        obj=Students(Student_name=S_name,Student_username=S_username,Student_email=S_email,Student_password=S_password,Student_address=S_address,Course_stream=S_course,date_of_reg=regdate)
        obj.save()
        return HttpResponse("created")