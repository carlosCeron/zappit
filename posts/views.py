from django.shortcuts import render
from rest_framework import generics, permissions
from posts.models import Post
from posts.serializers import PostSerializer


class PostList(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	
	def perform_create(self, serializer):
		serializer.save(poster=self.request.user)

