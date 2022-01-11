from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
import datetime
from django.http import JsonResponse

# Create your views here.
def ask(req):
    if not req.user.is_authenticated:
        return render(req, 'forbidden.html')

    if req.method == 'GET':
        return render(req, 'newpost.html')

    header = req.POST["header"]
    content = req.POST["content"]
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")

    postid = req.user.username[:8] + req.user.username[8::-1]
    post = Post.objects.create(user=req.user, postId=postid, heading=header, date=date, time=time,content=content)

    return HttpResponseRedirect('/')

def details(req, id):
    try:
        post = Post.objects.get(id=id)
        user = post.user
        response = {
            "id" : post.postId,
            "heading" : post.heading,
            "content" : post.content,
            "user" : {
                "first name" : user.first_name,
                "last name" : user.last_name,
                "email id" : user.email,
            }
        }

        return JsonResponse(response)
        
    except:
        return JsonResponse({
            "message" : "No post found with the provided id"
        })