from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer, VoteListSerializer

# Require to to pass the generics and import it

def home(request):
    #return render(request, 'index.html', {'content':PassTheObjectHere})
    return HttpResponse('Add view URL after api/ to access the API such as <a href=posts>Posts</a>')

# To create an object via API
class PostList(generics.ListCreateAPIView):
# To list an objects via API
#class PostList(generics.ListAPIView):
    # What objects you want to retrieve, Django automatically identify "queryset" variable and include it.
    queryset = Post.objects.all()
    # You must associate the serializer built for that model
    # Django automatically identify "serializer_class" variable and include it.
    serializer_class = PostSerializer

    # To specify who has call this API. Also, to prevent unlogged in people from calling the API
    #restrict all privilige to logged in users only
    #permission_classes = [permissions.IsAuthenticated]

    # Allow GET request to all guests but POST is restricted to authorized users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # To override function that will identify the user of the request
    # function name must be as same as below
    def perform_create(self, serializer):
        # This will identify the user id with the API to associate it. As we prevent user from passing the user ID manually before
        serializer.save(author_id=self.request.user.id)

class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # To know who is the user who is trying to vote for a post
        user = self.request.user

        # To know which post user is trying to vote or access, pk is coming from the URL (post he doesn't own)
        post = Post.objects.get(pk=self.kwargs['pk'])
        # Passed variables are identical with model naming. This will create a record in Vote model
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        # Check if user voted already or NOT. if yes, then system will prevent him from doing it twice
        if self.get_queryset().exists():
            raise ValidationError('You have voted to this Post already :)')
        # This will identify who is the user/voter (different than owner/author) and which post he is in
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))

class VoteList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]