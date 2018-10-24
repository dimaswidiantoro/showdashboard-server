from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.

@login_required
def analytics(request):
    return render(request,'analytics/analytics.html')
