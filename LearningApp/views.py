from django.shortcuts import render,redirect
import datetime
from LearningApp.models import Students,Student_course_Wishlist,Student_course_enrolment,Student_test_taken
from CourseApp.models import Courses
from TestApp.models import Tests
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from CourseApp.views import  Course_list

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')

#Student Functions

def Student_register(request):
    if request.method=='POST':
        S_name=request.POST.get('name')
        S_email=request.POST.get('email')
        S_username=request.POST.get('username')
        S_password=request.POST.get('password')
        S_address=request.POST.get('address')
        S_course=request.POST.get('course')
        regdate=datetime.datetime.today()
        obj=Students(Student_name=S_name,Student_username=S_username,Student_email=S_email,Student_password=S_password,Student_address=S_address,Course_stream=S_course,date_of_reg=regdate)
        obj.save()
        return redirect(login)
def Student_login(request):
     if request.method=='POST':
        user_name=request.POST.get('username')
        password=request.POST.get('password')
        if Students.objects.filter(Student_username=user_name,Student_password=password).exists():
            sdata=Students.objects.get(Student_username=user_name,Student_password=password)
            request.session['studentid']=sdata.id
            request.session['studentname']=sdata.Student_name
            return render(request,'index.html')
        else:
            return render(request,'login.html')

#wishlist Functions

def Wishlist_view(request):
    if 'studentid' in request.session:
        studentid=request.session.get('studentid')
        data=Student_course_Wishlist.objects.filter(student_id=Students.objects.get(id=studentid))
        return render(request,'wishlist.html',{'wishdata':data})



def Wishlist(request,cid):
    if 'studentid' in request.session:
        studentid=request.session.get('studentid')
        
        obj=Student_course_Wishlist(student_id=Students.objects.get(id=studentid),course_id= Courses.objects.get(id=cid))
        obj.save()
        messages.success(request, 'Add to wishlist successfully.')
        

        return render(request,'index.html')
    else:
        return redirect(login)
def wishlist_delete(request,dataid):
    data=Student_course_Wishlist.objects.filter(id=dataid)
    data.delete()
    return redirect(Wishlist_view)

#Course Registerations

def course_reglist(request):
    if 'studentid' in request.session:
        studentid=request.session.get('studentid')
        data=Student_course_enrolment.objects.filter(student_id=Students.objects.get(id=studentid))
        return render(request,'course_reglist.html',{'data':data})
    
def course_registeration(request,cid):
    if 'studentid' in request.session:
        studentid=request.session.get('studentid')
        date_entrollment=datetime.datetime.today()
        if Student_course_enrolment.objects.filter(student_id=Students.objects.get(id=studentid),course_id= Courses.objects.get(id=cid)).exists():
            messages.error(request, 'Course already registered')
            return redirect(Course_list)
        else:
        
            obj=Student_course_enrolment(student_id=Students.objects.get(id=studentid),course_id= Courses.objects.get(id=cid),date_entrollment=date_entrollment)
            obj.save()
            messages.success(request, 'Course Registered successfully')
            return redirect(course_reglist)
    else:
        return redirect(login)

#test taken functions

def test_taken_list(request):
    if 'studentid' in request.session:
        data=Student_test_taken.objects.filter(student_id=request.session.get('studentid'))
        return render(request,'test_taken_list.html',{'data':data})
def testlist(request,cid):
    if 'studentid' in request.session:
        data=Tests.objects.filter(Course_id__id=cid)
        return render(request,'testlist.html',{'data':data})
def test_taken(request,tid,cid):
    if 'studentid' in request.session:
        print("*****************",cid)
        studentid=request.session.get('studentid')
        if Student_test_taken.objects.filter(student_id=Students.objects.get(id=studentid),test_id=Tests.objects.get(id=tid)).exists():
            messages.error(request, 'you already completed the test!')
            return redirect(testlist,cid=cid)
        else:
            obj=Student_test_taken(student_id=Students.objects.get(id=studentid),test_id=Tests.objects.get(id=tid),test_status="completed")
            obj.save()
            messages.success(request, 'successfully completed the test!')
            return redirect(test_taken_list)
#student Profile

def student_profile(request):
    if 'studentid' in request.session:
        sdata=Students.objects.get(id=request.session.get('studentid'))
        Course_count=Student_course_enrolment.objects.filter(student_id=request.session.get('studentid')).count()
        whishlist_count=Student_course_Wishlist.objects.filter(student_id=request.session.get('studentid')).count()
        test_count=Student_test_taken.objects.filter(student_id=request.session.get('studentid'),test_status="completed").count()
        return render(request,'profile.html',{'sdata':sdata,'Course_count':Course_count,'whishlist_count':whishlist_count,'test_count':test_count})
#Logout 

def Student_logout(request):
    del request.session['studentid']
    del request.session['studentname']
    return redirect(index)

