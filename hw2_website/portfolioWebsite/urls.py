from django.contrib import admin
from django.urls import path, include
from . import views
# from .views import projectList

urlpatterns = [
    path('',views.home, name = 'home'),
    path('signUp', views.signUp, name = 'signUp'),
    path('signIn', views.signIn, name = 'signIn'),
    path('signout', views.signout, name = 'signout'),  
    path('main', views.main, name = 'main'),
]
