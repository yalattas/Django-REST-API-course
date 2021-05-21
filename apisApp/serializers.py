from rest_framework import serializers

# Import models that you need to seralize in order to pass it to different systems
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    # To prevent updating it via the API, only reading. Purpose: to prevent user from update another user data
    # source is what field value should be represented in the API. such as ['author':1] OR ['author':'yasser']
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')
    # to show total of votes. It will be passed to Meta by its name but calculated by the function below "get_votes"
    votesCount = serializers.SerializerMethodField()
    class Meta:
        # Reference the model that you need to serialize
        model = Post
        # What fields should be accessible by third-party app, author_id coming from the top
        fields = ['id', 'title', 'url', 'author', 'author_id', 'created_at', 'votesCount']
    # function must be same name as the variable, it our case "votes" see the following variable "votes = serializers.SerializerMethodField()"
    def get_votesCount(self, post):
        return Vote.objects.filter(post=post).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']

class VoteListSerializer(serializers.ModelSerializer):
    PostTitle = serializers.ReadOnlyField(source='post.title')
    class Meta:
        model = Vote
        fields = ['id', 'voter', 'post', 'PostTitle', 'created_at']