
from django.urls import path
from LearningApp import views

urlpatterns = [
    path('index',views.index,name='index')
]
   
