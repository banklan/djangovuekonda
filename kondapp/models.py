from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# class User(models.Model):
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
 