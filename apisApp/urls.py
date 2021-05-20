from apisApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

# For the front end to call this app and access its URLs
app_name = 'apisApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostList.as_view(), name='postsPath'),
    path('posts/<int:pk>/vote', views.VoteCreate.as_view(), name='AddVote'),

    path('votes/', views.VoteList.as_view(), name='votesPath'),
]