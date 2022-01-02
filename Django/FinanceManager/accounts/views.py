from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from funds.models import Fund

# Create your views here.
@csrf_protect
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully")
            return HttpResponseRedirect('/')

        else:
            messages.error(request, "Invalid credentials")
            return HttpResponseRedirect('/accounts/login/')

    if request.method == 'GET':
        return render(request, 'auth/login.html')

def logout(request):
    return render(request, 'auth/logout.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']

        users = User.objects.filter(username=username)
        if len(users) > 0:
            messages.success(request, "Username Exists")
            return HttpResponseRedirect('/accounts/register/')

        myUser = User.objects.create_user(username, email, password)
        myUser.first_name = fname
        myUser.last_name = lname


        myUser.save()

        fund = Fund.objects.create(user = request.user, spendables=0, savings=0)
        
        messages.success(request, "User Created")
        return HttpResponseRedirect('/accounts/login/')
        # messages.success(request, "Account has been created successfully")
    
    if request.method == 'GET':
        return render(request, 'auth/register.html')
