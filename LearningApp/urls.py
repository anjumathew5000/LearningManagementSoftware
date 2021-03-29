
from django.urls import path
from LearningApp import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('studentregister',views.Student_register,name='studentregister'),
    path('studentlogin',views.Student_login,name='studentlogin')
]
   
