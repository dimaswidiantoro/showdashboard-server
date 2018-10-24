from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.


def homepage(request):
    return render(request,'homepage/homepage.html')


def homepage2(request):
    return render(request,'homepage/homepage2.html')

@login_required
def halamandepan(request):
    return render(request,'homepage/halamandepan.html')

@login_required
def brainlyhttpool(request):
    return render(request,'homepage/brainlyhttpool.html')

@login_required
def internalteam(request):
    return render(request,'homepage/internalteam.html')
