from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request,'frontpage/frontpage.html')

def stakeholder(request):
    return render(request,'frontpage/stakeholder.html')
