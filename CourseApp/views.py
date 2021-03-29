from django.shortcuts import render

# Create your views here.
def Courselist(request):
    return render(request,'course_list.html')
