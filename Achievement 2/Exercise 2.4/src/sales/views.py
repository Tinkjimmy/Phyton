from django.shortcuts import render
from django.contrib.auth.decorators import login_required  #decorator required for function-based views


# Create your views here.
def home(request):
    return render(request,'sales/home.html')

@login_required  #adding the decorator to login-protect the view
def records(request):
    return render(request, 'sales/records.html')



