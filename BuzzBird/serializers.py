from rest_framework import serializers
from BuzzBird import models

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Post,
        fields=['body', 'time_posted', 'author']