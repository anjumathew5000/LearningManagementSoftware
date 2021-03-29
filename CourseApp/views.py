from django.shortcuts import render
from .models import Courses

# Create your views here.
def Course_list(request):
    course_data=Courses.objects.all()
    return render(request,'course_list.html',{'course_data':course_data})
