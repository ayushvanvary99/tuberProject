from django.urls import path

from .import views

urlpatterns=[
    path('teamform',views.teamform, name="teamform"),
   
    
]