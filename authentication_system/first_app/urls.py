from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.logIn, name='logIn'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logOut, name='logOut'),
    path('profile/edit_profile', views.edit_profile, name='edit_profile'),
    path('profile/change_pass', views.change_pass, name='change_pass'),
    path('profile/set_pass', views.set_pass, name='set_pass'),
]
