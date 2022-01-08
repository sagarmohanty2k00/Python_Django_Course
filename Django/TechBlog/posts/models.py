from django.contrib.auth.models import User
from django.db import models
from django.http.request import MediaType
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    postId = models.CharField(max_length=48)
    heading = models.CharField(max_length=48)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    content = models.TextField()

    def __str__(self):
        return self.postId


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    content = models.TextField()

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class PostTopic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)