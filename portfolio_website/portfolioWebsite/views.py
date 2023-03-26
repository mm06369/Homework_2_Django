from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request, 'authentication/index.html')

def signUp(request):

    if request.method == 'POST':
        name = request.POST['fname']
        usern = request.POST['usern']
        password = request.POST['password']
        email = request.POST['email']
        if email == None:
            email = 'NULL'
        if password == None:
            password = 'NULL'
        if usern == None:
            usern = 'NULL'
        if name == None:
            name = 'NULL'

        myUser = User.objects.create_user(usern, email, password)
        myUser.first_name = name
        myUser.last_name = name
        myUser.save()

        messages.success(request, 'Your account has been created')
        return redirect('main')
    
    return render(request,'authentication/signUp.html')

def signIn(request):

    if request.method == 'POST':
        username = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username = username,password =  pwd)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/main.html',{'fname':fname})
        else:
            messages.error(request, 'Bad Credentials')
            return redirect('home')

    
    return render(request,'authentication/signIn.html')

def signout(request):
    pass

def main(request):
    return render(request,'authentication/main.html')