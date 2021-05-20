from apisApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('posts/', views.PostList.as_view()),
]