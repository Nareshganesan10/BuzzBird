from django.shortcuts import render
from django.views import View
from BuzzBird.forms import PostForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie

from BuzzBird.models import Post
from BuzzBird.serializers import PostSerializers

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def home(request):
    post_list = Post.objects.all().order_by('-time_posted')
    if request.method != 'POST':
        return render(request, "authenticate/home.html", {
            "post_list": post_list,
        })
    elif request.method == 'POST':
        serializer = PostSerializers()

def signin(request):
    return render(request, "authenticate/signin.html", {})


def signup(request):
    return render(request, "authenticate/signup.html", {})


