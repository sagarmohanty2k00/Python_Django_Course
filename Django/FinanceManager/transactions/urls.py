from . import views
from django.urls import path

urlpatterns = [
    path('', views.transactions),
    path('add/<str:val>/', views.add),
    path('withdraw/<str:val>/<str:reason>/', views.withdraw),
    path('transfer/', views.transfer),
]