from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
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

        return redirect('signIn')
        

    return render(request,'authentication/signUp.html')

def signIn(request):
    return render(request,'authentication/signIn.html')

def signout(request):
    pass