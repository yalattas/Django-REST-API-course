from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post (models.Model):
    title = models.CharField(
        max_length=100
    )
    url = models.URLField()
    # Require User model to be imported
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    # To take current time and submit it
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # To list by the recent posts
        ordering = ['-created_at']

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)