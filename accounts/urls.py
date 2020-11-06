from django.urls import path
from .import views

app_name='accounts'

urlpatterns = [
    path('doctors/',views.doctors_list,name='doctors_list'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('profile/',views.myprofile,name='profile'),
    path('update/',views.update_profile,name='update_profile'),
    path('<slug:slug>/',views.doctors_details,name='doctors_details'),


   
]
