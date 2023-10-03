from django.urls import path
from . import views
from .views import *
from Tweet.views import AboutView 

urlpatterns = [
    path('create/', views.create_tweet),
    path('view/', views.view_tweet),
    path('delete/', views.delete_tweet),
    path('update/', views.update_tweet),
    path('createform/', views.createform_html), 
    path('shared_with/',views.shared_with),
    path('comment/',views.comment_form),

    path("listview/", TweetListView.as_view(), name="tweet-list"),
     path("tweet/<pk>/", TweetDetailView.as_view(), name="tweet-detail"),
     path("tweetcreate/", TweetCreateView.as_view(), name="tweet-create"),
     path("about/", AboutView.as_view()),
]
