from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

@login_required
def scindonesia(request):
    return render(request,'searchconsole/scindonesia.html')

@login_required
def scphilipines(request):
    return render(request,'searchconsole/scphilipines.html')

@login_required
def scfrance(request):
    return render(request,'searchconsole/scfrance.html')

@login_required
def scturkey(request):
    return render(request,'searchconsole/scturkey.html')
# Create your views here.
@login_required
def scindia(request):
    return render(request,'searchconsole/scindia.html')