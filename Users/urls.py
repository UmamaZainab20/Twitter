from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user),
    path('view/', views.view_user),
    path('delete/', views.delete_user),
    path('update/', views.update_user)

]
