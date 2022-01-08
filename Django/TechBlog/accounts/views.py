from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['email']
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
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'logout.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']

        users = User.objects.filter(username=username)
        if len(users) > 0:
            messages.error(request, "Username Exists")
            return HttpResponseRedirect('/accounts/register/')

        myUser = User.objects.create_user(username, username, password)
        myUser.first_name = fname
        myUser.last_name = lname


        myUser.save()
        
        messages.success(request, "User Created")
        return HttpResponseRedirect('/accounts/login/')
    
    if request.method == 'GET':
        return render(request, 'register.html')

def changePassword(req):
    password = req.POST['password']
    newPassword = req.POST['newPassword']

    user = authenticate(username=req.user.username, password=password)

    if user is not None:
        user.set_password(newPassword)
        return HttpResponseRedirect('/')

    else:
        messages.error(req, "Invalid credentials")
        return HttpResponseRedirect('/accounts/changepassword/')


def updateUser(req):
    user = CustomUser.objectas.get(user=req.user)

    user.github = req.POST['github']
    user.instagram = req.POST['instagram']
    user.linkedin = req.POST['linkedin']
    user.address = req.POST['address']
    user.organization = req.POST['organization']
    req.user.first_name = req.POST['firstName']
    req.user.last_nmae = req.POST['lastNmae']

    user.save()
    req.user.save()

    redirectLink = '/accounts/profile/' + str(user.id) + '/'

    return HttpResponseRedirect(redirectLink)


def userProfile(req, id):
    user = User.objects.get(id=id)
    customUser = CustomUser.objects.get(user=user)

    return render(req, 'user.html', {
        'user' : user,
        'otherInfo' : customUser,
    })