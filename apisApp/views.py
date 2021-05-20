from django.shortcuts import render, HttpResponse
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

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
        # This will page the user id with the API to associate it. As we prevent user from passing the user ID manually before
        serializer.save(author_id=self.request.user.id)