from django.urls import path
from .import views

app_name='accounts'

urlpatterns = [
    path('doctors/',views.doctors_list,name='doctors_list'),
    path('<slug:slug>/',views.doctors_details,name='doctors_details'),

   
]
