from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PostModel(models.Model):
    time_posted = models.DateField(default=timezone.now)
    body = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.body)
