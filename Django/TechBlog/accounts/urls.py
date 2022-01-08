from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser),
    path('logout/', views.logoutUser),
    path('register/', views.register),
    path('changePassword/', views.changePassword),
    path('updateUser/', views.updateUser),
    path('userProfile/<int:id>/', views.userProfile),
]