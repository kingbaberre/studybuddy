from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Topic, Reply
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    name =  get_username()
    mytopics = Topic.objects.get(username=name)
    return request,'discussion/index',{mytopics:'topics'}
