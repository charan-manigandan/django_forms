from django.shortcuts import render, redirect
from urllib import request
from django.views import View
from django.contrib import messages
from django.conf import settings
from django.db.models import Count
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from . models import *
from . forms import *
from django.db.models import Q
from django.contrib.auth import authenticate

# Create your views here.
def HomePage(requests):
    disp = Feedback.objects.all()
    return render(requests, 'home.html',{'disp': disp})

    
def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        obj = Feedback(name=name, email=email, feedback=feedback)
        obj.save()
        return render(request, 'home.html')
    return render(request, 'feedback.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! User Registration Success')
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'customerregistration.html', locals())
    
class CustomerVerified(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'home.html', locals())
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Login Successful')
        else:
            messages.error(request, 'Invalid Login credentials Try again!')
        return 
    
class ProfileView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'profile.html', locals())

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            form.save()
            return redirect('profile.html', locals())
            messages.success(request, 'congratulations! Profile Save successfully')
        else:
            messages.warning(request, 'Invalid Input Data')
        return render(request, 'profile.html', locals())