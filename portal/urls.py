from portal import views
from django.urls import path


app_name = 'portal'

urlpatterns = [
    path('', views.home, name='home'),
]
