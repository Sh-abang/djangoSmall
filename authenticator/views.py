from django.shortcuts import render, redirect #, get_object_or_404, get_list_or_404
# from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from diary.models import MyUser

def log_in(request):

    if request.method =='POST':

        password = request.POST['password']
        email = request.POST['email']
        # sort out username vs email login
        author_user = authenticate(username=email, password=password)
        if author_user is not None:
            login(request, author_user)
            return redirect('index')
        
    return render(request, 'authenticator/login.html')
    # else:

    #     return HttpResponseRedirect (('login'))

def log_out(request):
    logout(request)
    return redirect('login')

def register(request):

    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        dob = request.POST['dob']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            author_user= MyUser.objects.create_user(user_name=username,email=email,first_name=firstName,last_name=lastName,dob=dob,password=password1)
            # objects.create_user(username=custom_username,email=email,password=password1,first_name=firstName,last_name=lastName)
            author_user.save
        else:
            messages.info(request,'Passwords do not match')
            return render(request, 'authenticator/register.html')

        return redirect ('index')
    else:
        return render(request, 'authenticator/register.html')
    