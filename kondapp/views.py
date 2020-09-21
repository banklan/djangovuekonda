from django.shortcuts import render
from rest_framework import viewsets, status, serializers

from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        id = self.kwargs.get('pk')
        post = self.get_queryset().get(id=id)
        return post
