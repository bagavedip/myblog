from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from blog.serializers import UserSerializer, PostSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .models import Post
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
