from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.

def doctors_list(request):
    doctor =User.objects.all()

    return render(request,'user/doctors_list.html',{'doctor':doctor})

def doctors_details(request , slug):
    doctors_details =Profile.objects.get(slug=slug)

    return render(request,'user/doctors_detail.html',{'doctors_details':doctors_details})
