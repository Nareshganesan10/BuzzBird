from rest_framework import serializers
from BuzzBird import models

class PostSerializers():
    class Meta:
        model = models.PostModel
        fields = ['time_posted, body', 'username', 'post_id']