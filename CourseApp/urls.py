
from django.urls import path
from CourseApp import views


urlpatterns = [
    path('courselist',views.Course_list,name="courselist")
    
]
