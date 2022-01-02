from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('404/', views.notFound),
    path('invalid-request/', views.invalid),
]