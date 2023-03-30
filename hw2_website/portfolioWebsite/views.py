from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from .models import Project
# Create your views here.

def home(request):
    return render(request, 'authentication/index.html')

def signUp(request):

    if request.method == 'POST':
        name = request.POST['fname']
        email = request.POST['email']
        password = request.POST['password']
        if password == None:
            password = 'NULL'
        if email == None:
            email = 'NULL'
        if name == None:
            name = 'NULL'

        try:
            myUser = User.objects.create_user(email,email, password)
            myUser.first_name = name
            myUser.last_name = name
            myUser.save()

            messages.success(request, 'Your account has been created')
            return redirect('signIn')

        except:
            messages.error(request, 'Error creating account')

    return render(request,'authentication/signUp.html')

def signIn(request):

    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = authenticate(username = email ,password =  pwd)

        if user is not None:
            login(request, user)
            fname = user.first_name
            # return render(request, 'authentication/main.html',{'fname':fname})
            # return redirect('projectList')
            projects = Project.objects.filter(user=user)
            return render(request, 'authentication/main.html', {'fname':fname,'object_list': projects, 'show':True})
        else:
            messages.error(request, 'Bad Credentials')
            return redirect('home')

    
    return render(request,'authentication/signIn.html')

# class projectList(ListView):
#     model = Project
#     template_name = 'authentication/main.html'
#     # fname = 

# def projects_list(request):
#     c

def signOut(request):
    try:
        logout(request)
        return redirect('home')
    except:
        messages.error(request, 'Error Signing out')
        user = request.user
        projects = Project.objects.filter(user=user)
        return render(request, 'authentication/main.html', {'fname':user.first_name,'object_list': projects})
    
def main(request):

    if request.method == 'POST':
        project_name = request.POST['project-name']
        description = request.POST['description']
        media = request.FILES['media-file']

        newProject =  Project(user = request.user, title = project_name, description = description, media = media)
        newProject.save()

    user = request.user
    projects = Project.objects.filter(user=user)
    return render(request, 'authentication/main.html', {'fname':user.first_name,'object_list': projects, 'show':True})
        

def guestSignIn(request):
    projects = Project.objects.filter()
    return render(request, 'authentication/main.html', {'fname':'Guest User','object_list': projects, 'show':False})
