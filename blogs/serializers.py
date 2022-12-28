from .models import Posts
from rest_framework import serializers

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


