from django.urls import path
from BuzzBird import views

urlpatterns = [
    path("home/", view=views.home, name="home"),
    path("signin/", view=views.signin, name="signin"),
    path("signup/", view=views.signup, name="signup"),
    path("signout/", view=views.signout, name="signout"),
    path("search/", view=views.search, name="search"),
    path("delete_post/<str:username>", view=views.delete_post, name="delete_post"),
    path("follow/<str:username>", view=views.follow, name="follow"),
    path("unfollow/<str:username>", view=views.unfollow, name="unfollow"),
]
