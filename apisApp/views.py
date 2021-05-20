from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Require to to pass the generics and import it

def home(request):
    #return render(request, 'index.html', {'content':PassTheObjectHere})
    return HttpResponse('Add view URL after api/ to access the API such as <a href=posts>Posts</a>')

class PostList(generics.ListAPIView):
    # What objects you want to retrieve, Django automatically identify "queryset" variable and include it.
    queryset = Post.objects.all()
    # You must associate the serializer built for that model
    # Django automatically identify "serializer_class" variable and include it.
    serializer_class = PostSerializer