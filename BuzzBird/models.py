from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PostModel(models.Model):
    post_id = models.AutoField(primary_key=True)
    time_posted = models.DateField(default=timezone.now)
    body = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, default='username')
    

    def __str__(self):
        return(self.body)


class ProfileModel(models.Model):
    follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow")
    fololowed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.fololowed_by)