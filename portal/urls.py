from portal import views
from django.urls import path

# For the front end to call this app and access its URLs
app_name = 'portal'

urlpatterns = [
    path('', views.home, name='home'),
]
