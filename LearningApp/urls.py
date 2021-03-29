
from django.urls import path
from LearningApp import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('studentregister',views.Student_register,name='studentregister'),
    path('studentlogin',views.Student_login,name='studentlogin'),
    path('studentlogout',views.Student_logout,name='studentlogout'),
    path('wishlist/<int:cid>/',views.Wishlist,name='wishlist'),
    path('course_registeration/<int:cid>/',views.course_registeration,name='course_registeration'),
    path('course_reglist/',views.course_reglist,name='course_reglist')
]

   
