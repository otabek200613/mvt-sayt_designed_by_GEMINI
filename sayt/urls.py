from django.urls import path

from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('profile/',profile,name='profile'),
    path('logout/',logout_view,name='logout'),
    path('register/',register,name='register'),
    path('login/',login_view,name='login'),
    path('blog/<int:pk>/',blog,name='blog'),
    path('profile_change/',profile_change,name='profile_change'),
    path('change_password/',change_password,name='change_password'),


]