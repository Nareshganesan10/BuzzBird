from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField()
    time_posted = models.DateField(default=timezone.now)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.body)