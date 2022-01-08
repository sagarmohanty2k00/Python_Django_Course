from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('feed/<int:postNum>/', views.feed),
    path('search/<str:query>/', views.search),
    path('topic/<str:query>/', views.topic),
]