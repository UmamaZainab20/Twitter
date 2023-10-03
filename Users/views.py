from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
 
# Create your views here.
@csrf_exempt
def create_user(request):
    data = request.body
    data = json.loads(data.decode('utf-8'))
    name = data['name']
    email = data['email']
    username = data['username']
    p1 = User(name = name, email = email, username = username)
    p1.save()

    return JsonResponse(data)

def view_user(request):
    username = request.GET.get("username")
    user = User.objects.get(username = username)
    return HttpResponse(user)

def delete_user(request):
    name = request.GET.get("username")
    user = User.objects.get(username = name)
    user.delete()
    return HttpResponse("deleted")

@csrf_exempt
def update_user(request):
    username = request.GET.get("username")
    user = get_object_or_404(User, username = username)
    data = request.body
    data = json.loads(data.decode('utf-8'))
    user.name = data['name']
    user.email = data['email']
    user.save()
    return HttpResponse("successfully")