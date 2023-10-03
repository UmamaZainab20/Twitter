from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse , HttpResponse
import json
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from Users.models import User
from .models import Tweet
from django import forms

# Create your views here.
@csrf_exempt
def create_tweet(request):

    data = request.body
    data = json.loads(data.decode('utf-8'))
    username = data["username"]
    name = data["name"]
    content = data["content"]
    user = User.objects.get(username = username)
    tweet = Tweet(user = user, name = name, content = content)
    tweet.save()
    
    response = {
        "message": "Success",
        "data": {
            "title": tweet.name,
            "content": tweet.content
        }
    }
    return JsonResponse(response)

def view_tweet(request):
    username = request.GET.get("username")
    name = request.GET.get("name")
    user = User.objects.get(username = username)
    tweet = Tweet.objects.get(user = user, name= name)
    return HttpResponse(tweet)
    
    
def delete_tweet(request):
    user_id = request.GET.get("user_id")
    name = request.GET.get("name")
    user = User.objects.get(id = user_id)
    tweet = Tweet.objects.get(user = user,name = name)
    tweet.delete()
    return HttpResponse("deleted")

@csrf_exempt
def update_tweet(request):
    
    username = request.GET.get("username")
    name = request.GET.get("name")

    user = User.objects.get(username = username)
    tweet = Tweet.objects.get(user=user,name=name)

    data = json.loads(request.body.decode('utf-8'))
    
   
    tweet.name = data["name"]

    tweet.content = data["content"]
        
    tweet.save()

    return HttpResponse("successful")    


class form_for_tweet(forms.Form):
    user = forms.CharField(required=True)
    name  = forms.CharField(label= "Name  of your tweet", required=True,max_length=50)
    content = forms.CharField(required=True, label= "Content")
    file = forms.FileField()


def createform_html(request):
    if request.method == "GET":
        form = form_for_tweet()
        return render(request,"tweets/form.html",{"form":form})

    if request.method == "POST":
        form = form_for_tweet(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            content = form.cleaned_data["content"]
            user = form.cleaned_data["user"]
            file = form.cleaned_data["file"]
            person = User.objects.get(username = user)
            tweet = Tweet(user = person, name = name, content = content, media = file)
            tweet.save()
        else:
            return render(request,"tweets/form.html",{"form":form})
    
    return HttpResponse("done")


class Shared_with(forms.Form):
    user = forms.CharField(label= "Name  of your user",required=True)
    tweet_name  = forms.CharField(label= "Name  of your tweet", required=True,max_length=50)

def shared_with(request):
    if request.method == "GET":
        form = Shared_with()
        return render(request,"tweets/form_share.html",{"form":form})

    if request.method == "POST":
        form = Shared_with(request.POST)
        if form.is_valid():
            tweet_name = form.cleaned_data["tweet_name"]
            user = form.cleaned_data["user"]
            person = User.objects.get(username = user)
            tweet = Tweet.objects.get(name = tweet_name)
            tweet.shared_with.add(person)
            
        else:
            return render(request,"tweets/form_share.html",{"form":form})
    
    return HttpResponse("shared to xyz")


from .forms import Comment_Form

# for commenting on tweet we GET the data first and then POST a coment on it
def comment_form(request):
    if request.method == "GET":
        form = Comment_Form()
        return render(request,"tweets/comment.html",{"form":form})

    if request.method == "POST":
        form = Comment_Form(request.POST)
        form.save()
            
    else:
        return render(request,"tweets/comment.html",{"form":form})
    
    return HttpResponse("Comment Done")



class TweetListView(ListView):
    model = Tweet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class TweetDetailView(DetailView):
    model = Tweet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class TweetCreateView(CreateView):
    model = Tweet
    fields = ["name","user","content"]


# 
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "tweets/about_template.html"