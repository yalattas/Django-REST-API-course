from rest_framework import serializers

# Import models that you need to seralize in order to pass it to different systems
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # Reference the model that you need to serialize
        model = Post
        # What fields should be accessible by third-party app
        fields = ['id', 'title', 'url', 'auther', 'created_at']