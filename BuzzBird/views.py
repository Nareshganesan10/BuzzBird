from django.shortcuts import render, redirect
from BuzzBird.models import PostModel
from BuzzBird.serializers import PostSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import PostForm
from django.utils import timezone
from BuzzBird.models import FollowModel


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def home(request):
    posts = PostModel.objects.all().order_by('-time_posted')
    form = PostForm()
    if request.method == 'GET':
        form = PostForm(request.GET)

    elif request.method != 'POST':
        return render(request, "authenticate/home.html", {
            "posts": posts,
        })
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.username_id = request.user.id
            new_post.save()
            messages.success(request, "Posted")
            return redirect("home")
        messages.success(request, "Posted")
        return redirect('home')
    context = {
        'form': form,
        'posts': posts,
    }
    return render(request, "authenticate/home.html",context)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Logged in")
            return redirect('home')
        else:
            messages.success(request, "incorrect username or password")
            return redirect('home')
    return render(request, "authenticate/signin.html", {})



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        retype_password=request.POST.get('retype_password')
        username = request.POST.get('username')
        if password ==  retype_password:
            if User.objects.filter(email=mail).exists():
                messages.success(request, "request,Email already exists, Please try with another email")
                return redirect('signup')
            else:
                user =  User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=mail)
                user.set_password(password)
                user.save()
                messages.success(request, "Account succesfully created")
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    login(request, new_user)
                    messages.success(request,"Logged in")
                    return redirect('home')
                return redirect('signup')
                messages.success(request,"Error with the data, please verufy once again")
        else:
            messages.success(request,"password and Password confirmation did not match")
            return redirect('signup')
    messages.success(request,"Error with the data, please verufy once again")
    return render(request, "authenticate/signup.html", {})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def signout(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('signin')


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def search(request):
    if request.method == 'POST':
        searched_username =  request.POST.get('username')
    elif request.method == 'GET':
        searched_username = request.user
    posts = PostModel.objects.filter(username__username=searched_username).values().order_by('-time_posted')
    #following_values = People the user is following
    following_values = list(FollowModel.objects.filter(username=str(request.user)).values_list('follows', flat=True))
    #follower_values = The people that follows the user
    follower_values = list(FollowModel.objects.filter(follows=str(request.user)).values_list('username', flat=True))
    number_of_posts = len(posts)
    print(following_values)
    print(follower_values)
    return render(request, "authenticate/profile.html", {
        'user': str(request.user),
        'posts': posts,
        'number_of_posts': number_of_posts,
        'username': searched_username,
        'following': following_values,
        'followers': follower_values,
    })        



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def delete_post(request):
    pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def follow(request, username):
    if request.user.is_authenticated:
        user = User.objects.filter(username=username).first()
        follow = FollowModel.objects.create(follows=str(user), username=str(request.user), follower=None)
        follow.save()
        messages.success(request, "You are following" + str(username))
    return redirect('search') 