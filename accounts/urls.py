from django.urls import path
from .import views

app_name='accounts'

urlpatterns = [
    path('app/',views.account,name='app')
   
]
