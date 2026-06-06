from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        User.objects.create_user(
            username = username,
            password = password,
            email = email
        )

        return redirect('login')
    return render(request,'register.html')



def loginview(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username= username,password = password)
        if user :
            login(request,user)
            return redirect('dashboard')
    return render(request,'login.html')
