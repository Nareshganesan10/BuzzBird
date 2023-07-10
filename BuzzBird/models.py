from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user

#for all the Posts
class PostModel(models.Model):
    post_id = models.AutoField(primary_key=True)
    time_posted = models.DateField(default=timezone.now)
    body = models.TextField()
    username = models.CharField(max_length=50)
    # username_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.body)


#User model
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', max_length=255)

    def __str__(self):
        return str("Following "+ str(self.follows))


#for Follow and Unfollow functions
class FollowModel(models.Model):
    follower = models.CharField(max_length=50, null=True)
    follows = models.CharField(max_length=50, null=True)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str("Following "+ str(self.follows))