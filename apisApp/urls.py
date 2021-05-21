from apisApp import views
from django.urls import path

# For the front end to call this app and access its URLs
app_name = 'apisApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostList.as_view(), name='postsPath'), # You can add a post from here
    path('posts/<int:pk>', views.PostRetrieveDestroy.as_view(), name='DeletePost'),
    path('posts/<int:pk>/vote', views.VoteCreate.as_view(), name='AddVote'),

    path('votes/', views.VoteList.as_view(), name='votesPath'),

]