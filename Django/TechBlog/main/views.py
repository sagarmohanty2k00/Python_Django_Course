from django.shortcuts import render
from posts.models import Post, Topic

# Create your views here.
def home(req):
    posts = Post.objects.all()[:10]
    tags = Topic.objects.all()

    return render(req, 'index.html', {
        'posts' : posts,
        'tags' : tags,
    })

def feed(req, postNum):
    return render(req, 'index.html', {'postNum':postNum})

def search(req, query):
    posts = Post.objects.all()
    all_post = []
    for post in posts:
        if query in post.heading:
            all_post.append(post)

def topic(req, query):
    pass